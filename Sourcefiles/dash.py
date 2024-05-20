import os
import cv2 as cv
import webbrowser
import shutil


def copy(src, dst):
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.copyfile(src, dst)

def save(path, image, jpg_quality=None):
  if jpg_quality:
    cv.imwrite(path, image, [int(cv.IMWRITE_JPEG_QUALITY), jpg_quality])


def resizeImage(path,resizeimgPath,resizeImgHeight):
	im = cv.imread(path)
	if im is None:
		raise ValueError("Invalid Image Path !!!")

	image_h, image_w = im.shape[:2]
	aspect_ratio = image_w / float(image_h)
	if image_w < image_h:
		new_height = resizeImgHeight
		new_width = int(aspect_ratio * new_height)
	else:
		new_width = resizeImgHeight
		new_height = int(new_width / aspect_ratio)

	resized_im = cv.resize(im,(new_width, new_height),interpolation=cv.INTER_NEAREST)
	cv.imwrite(resizeimgPath,resized_im)


def copy_in_to_resize_dir(dir,resizedDir,resizeImgHeight=600):
	imgFiles = os.listdir(dir)
	imgFiles.sort()
	# print(imgFiles)
	for idx, img in enumerate(imgFiles):
		# print(os.path.basename(img))
		if os.path.basename(img) == "desktop.jpg":
			os.remove(os.path.join(dir,img))
		imgPath = os.path.join(dir,img)
		if idx % 2 == 0:
			resizeimgPath = os.path.join(resizedDir, os.path.splitext(os.path.basename(img))[0] + ".jpg")
		elif idx % 2 != 0:
			resizeimgPath = os.path.join(resizedDir, os.path.splitext(os.path.basename(img))[0] + ".png")
		# print(f"resizeimgPath: {resizeimgPath}")
		
		resizeImage(imgPath,resizeimgPath,resizeImgHeight)
		# elif img.lower().endswith(('.png')):
		# 	if os.path.splitext(os.path.basename(img))[0].lower().endswith(('.jpg','.jpeg','.png', '.tif', '.tiff', '.bmp')):
		# 		resizeimgPath = os.path.splitext(os.path.splitext(os.path.basename(img))[0])[0]
		# 		resizeimgPath = os.path.join(resizedDir, os.path.splitext(os.path.basename(resizeimgPath))[0] + ".png")
		# 	newPath = resizeimgPath + ".png"
		# 	shutil.copy2(imgPath,newPath)

def get_orig_img_path_with_ext(img,orig_dir,exts):
	img_no_ext = os.path.splitext(os.path.basename(img))[0]
	orig_img_path = img
	for ext in exts:
		if os.path.isfile(os.path.join(orig_dir,img_no_ext + ext)):
			orig_img_path = os.path.join(os.path.abspath(orig_dir),img_no_ext + ext)
			break
	return orig_img_path

def attach_common():
	return ' '

def insert_images(input_img_dir,origInputDir, pipeline_nodes_orig_dir,pipeline_nodes,unsupported_keywords,window_height=367, startPath = None):
	message = ''
	input_img_files = os.listdir(origInputDir)
	# print(len(input_img_files))
	count = 0
	exts = ('.jpg','.jpeg','.png', '.tif', '.tiff', '.bmp')
	validTr = ''
	invalidTr = ''
	isValid = False
	isInvalid = False

	count_imgs_valid = 1

	even_img = []
	odd_img = []
	for i in range(len(input_img_files)):
		if i % 2 == 0:
			even_img.append(input_img_files[i])
		else:
			odd_img.append(input_img_files[i])
	
    
	print(even_img)
	print(odd_img)
    
	count1 = 0
	count2 = 0
	for i in range(len(input_img_files)):
		# print(len(input_img_files))
		tr = '<tr>'
		# insert_tr = True
		
		if i % 2 == 0:
			img = even_img[count1]
			count1 += 1
		
			in_img = cv.imread(os.path.join(os.path.abspath(input_img_dir),img))
			height =  in_img.shape[0]
			width =  in_img.shape[1]
			aspect_ratio = float(width) / float(height)
			new_height_input = window_height
			new_width_input = int(new_height_input * aspect_ratio)
			orig_img = os.path.basename(get_orig_img_path_with_ext(img,os.path.abspath(origInputDir), '.jpg'))
			td_input ='''<td rowspan="1" border="9" style="border-style: solid;border-color:''' + "black" + ''';border-width: 10px 10px 10px 10px;border-left: 6px solid gray;padding: 30px;vertical-align:top;border-bottom: 6px solid gray;"><a href="'''+ os.path.join(os.path.relpath(orgInputDir, startPath),orig_img).replace("\\","/") + '''"''' +'''><img src="''' + os.path.join(os.path.relpath(input_img_dir, startPath),img).replace("\\","/") + '''"''' + attach_common() + "height="+'"'+str(new_height_input)+'"' + "width="+'"'+str(new_width_input)+'"'+"></img></a></td>"
		
		elif i % 2 != 0:
			img = odd_img[count2]
			count2 += 1

			msk = cv.imread(os.path.join(os.path.abspath(input_img_dir),img))
			height =  msk.shape[0]
			width =  msk.shape[1]
			aspect_ratio = float(width) / float(height)
			new_height_input = window_height
			new_width_input = int(new_height_input * aspect_ratio)
			msk_img = os.path.basename(get_orig_img_path_with_ext(img,os.path.abspath(orgInputDir), '.png'))
			td_input += '''<td rowspan="1" border="9" style="border-style: solid;border-color:''' + "black" + ''';border-width: 10px 10px 10px 10px;border-left: 6px solid gray;padding: 30px;vertical-align:top;border-bottom: 6px solid gray;"><a href="'''+ os.path.join(os.path.relpath(orgInputDir, startPath),msk_img).replace("\\","/") + '''"''' +'''><img src="''' + os.path.join(os.path.relpath(input_img_dir, startPath),img).replace("\\","/") + '''"''' + attach_common() + "height="+'"'+str(new_height_input)+'"' + "width="+'"'+str(new_width_input)+'"'+"></img></a></td>"
			tr += td_input
			tr +=  '</tr>'
		
		

		message += tr
		# if insert_tr:
		# 	message += tr
		# 	count_imgs_valid += 1
	return message

def generate_html(title, input_dir, origInputDir, pipeline_nodes_dir,pipeline_nodes_heading,pipeline_nodes_orig_dir,pipeline_nodes_heading_colors, versionInfo,unsupported_keywords, startPath,window_height):
	message =''
	
	if len(pipeline_nodes_dir) != len(pipeline_nodes_heading) != len(pipeline_nodes_heading_colors):
		print("pipeline_nodes_dir and pipeline_nodes_heading must be same size")
		return message

	message +='<!DOCTYPE html>\n'
	message += """<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">""" + "<title>" + title + "</title>" + \
	"""</head>
	<body style="border-style: solid;border-color: black;margin-left:auto;margin-right:auto;"> """ + """<h1 align="center" style="color:white;">""" + title + "</h1>" + \
	 """<table align="center" style="border-style: solid;border-color: black;" border="3" cellspacing="15">
			<tr style="border-color: white;">
			  <th style="border-style: solid;border-color: white; border-width: 5px 5px 5px 5px;font-size: x-large;color:Black;">Input Image</th>
			  <th style="border-style: solid;border-color: green; border-width: 5px 5px 5px 5px;font-size: x-large;color:black;">Mask Image</th>""" 

	for heading,version,color in zip(pipeline_nodes_heading,versionInfo,pipeline_nodes_heading_colors):
		message +=	"""<th style="border-style: solid;border-color:""" + color+""";border-width: 5px 5px 5px 5px;font-size: x-large;color:white;">"""
		message += """<div style="font-size: x-large;color:white;">"""+str(heading)+"</div>"
		message += """<div style="font-size:15px;">"""+str(version)+"</div>"
		message += "</th>"
		
	message +=		"</tr>"

	#pipeline_nodes_heading_colors = ["coral","green", "red", "coral"]

	img_tr = insert_images(input_dir,origInputDir, pipeline_nodes_orig_dir,pipeline_nodes_dir,unsupported_keywords,window_height=window_height, startPath = startPath)
	message += img_tr
	message += "</table>"
	message += "</body>"
	message += "</html>"
	return message

def classifyLabels(orgInputDir, htmlDir, inputDir, title):
    performanceData = []
    unsupported_keywords = []

    bool = True

    resizeInput = True
    resizedInputDir = None

    open_in_browser = True
    resizeImgHeight = 480
    windowHeight = 480
    resizeExt=".jpg"

    if not os.path.isdir(inputDir):
        os.mkdir(inputDir)	

    if not os.path.isdir(htmlDir):
        os.mkdir(htmlDir)

    imgFiles = os.listdir(orgInputDir)
    if bool:
        for img in imgFiles:
            if img.lower().endswith('.jpg'):
                # print("\n\n" + img + "\n")
                imgPath = os.path.join(orgInputDir,img)
                copyImgPath = os.path.join(inputDir, img)

                inputImg = cv.imread(imgPath, cv.IMREAD_UNCHANGED)
                imgName = img.split('.')[0] + ".jpg"
                save(os.path.join(inputDir, imgName), inputImg, 70)
                
            
            elif img.lower().endswith('.png'):
                maskPath = os.path.join(orgInputDir,img)
                copy(maskPath, inputDir)
    

    if resizeInput:
        print("---------------Resizing Input-------------------")
        resizedInputDir = os.path.join(htmlDir,"inputResized")
        if not os.path.isdir(resizedInputDir):
            os.mkdir(resizedInputDir)
        copy_in_to_resize_dir(orgInputDir,resizedInputDir,resizeImgHeight)
    else:
        resizedInputDir = orgInputDir

    outImgFolderPaths = []
    outImgOrigFolderPaths = []
    outImgFolderNames = []
    versionInfo = []


    pipeline_nodes_heading_colors = ["green"]
    pipeline_nodes_heading_colors.insert(0,"aqua")

    print("---------------Generating Dashboard-------------------")


    message = ''
    message = generate_html(title, resizedInputDir, orgInputDir, outImgFolderPaths,outImgFolderNames,outImgOrigFolderPaths,pipeline_nodes_heading_colors,versionInfo,unsupported_keywords, htmlDir, windowHeight)
    if message == '':
        print("Dashboard generation failed")
        exit(2)

    f = open(htmlDir+ '\\index.html','w')
    f.write(message)
    f.close()
    if open_in_browser:
        webbrowser.open_new_tab(htmlDir+ '\\index.html')
        open_in_browser = False
    
    return performanceData

def createDir(orgInputDir, outputDir):
    inputDir = os.path.abspath(os.path.join(outputDir, "Input"))
    htmlDir = os.path.abspath(os.path.join(outputDir, "html"))
        
    title = "Targets51"
    performanceDataTemp = classifyLabels(orgInputDir, htmlDir, inputDir, title)



if __name__ == "__main__":
    orgInputDir = "C:\\Users\\ChNa395\\Desktop\\Targets51\\masks"
    outputDir = "C:\\Users\\ChNa395\\Desktop\\Dash1"
                      
    createDir(orgInputDir, outputDir)
