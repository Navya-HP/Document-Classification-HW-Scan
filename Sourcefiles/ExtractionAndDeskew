# DESKEW and EXTRACT images from the given images


import cv2 as cv
import numpy as np
import os
DUMP_PATH = 'C:\\Users\\ChNa395\\python\\BatchRun\\Dump\\AllTargetsDump\\DeskewedTargets\\'


def getRect(image):
    _, thresh = cv.threshold(image, 0, 255, cv.THRESH_BINARY)
    # cv.imwrite(DUMP_PATH + "thrresh.png", thresh)
    contours, _ = cv.findContours(thresh, mode = cv.RETR_EXTERNAL, method = cv.CHAIN_APPROX_SIMPLE)	
    # cv.drawContours(image, contours, -1, (255, 255, 0), 2)
    contour = max(contours, key=cv.contourArea)
    colorImg = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
    colorImg1 = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
    hull = cv.convexHull(contour, clockwise=True)
    # cv.drawContours(colorImg, [hull], -1, (255, 255, 0), 5)
    # cv.imwrite(DUMP_PATH  + "contour.png", colorImg)
  
    rotRect = cv.minAreaRect(hull)
    rect1 = rotRect
    # rect_points = np.array([[x, y], [x+w, y], [x+w, y+h], [x, y+h]])
    # rect1 = cv.minAreaRect(rect_points)
    box = cv.boxPoints(rotRect)
    box = np.intp(box)
    cv.drawContours(colorImg1, [box], 0, (0,0,255), 5)
    # rectImg = cv.rectangle(colorImg1, (int(rect1[0][0]), int(rect1[0][1])), (int(rect1[0][0] + rect1[1][0]), int(rect1[0][1] + rect1[1][1])), (0, 255, 0), 2)
    # cv.imwrite(DUMP_PATH  + "rectImg.png", colorImg1)
    
    angle = rect1[2]
    if abs(angle) > 45.0:
        angle = (-1) * (90 - abs(angle))
    return rect1, angle


def imageExtraction(img, img1):
    cntrs, _ = cv.findContours(img1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    list_extracted_images = []

    for contour in cntrs:
        min_x, min_y, max_x, max_y = cv.boundingRect(contour)
        region_of_interest = img1[min_y: min_y + max_y, min_x :min_x + max_x]
        region_of_interest_image = img[min_y: min_y + max_y , min_x :min_x + max_x]
        list_extracted_images.append(region_of_interest_image)
        image = region_of_interest
        rect, angle = getRect(image)
        matrix = cv.getRotationMatrix2D(((image.shape[1])/2,(image.shape[0])/2),angle,1)
        rotated_image = cv.warpAffine(region_of_interest_image, matrix, (image.shape[1],image.shape[0]), borderMode = cv.BORDER_CONSTANT, borderValue = 0)
        # cv.imwrite(DUMP_PATH  + "rotated_image.png", rotated_image)
        box = cv.boxPoints(rect)
        points = np.intp(cv.transform(np.array([box]), matrix))[0]
        points[points < 0] = 0
        if(angle > 0):
            cropped_image = rotated_image[points[1][1]:points[0][1], points[1][0]:points[2][0]]
        elif angle == 0:
            continue
        else:
            cropped_image = rotated_image[points[0][1]:points[2][1], points[0][0]:points[2][0]]
        list_final_images.append(cropped_image)
    return list_extracted_images



input_dir = 'C:\\Users\\ChNa395\\Desktop\\Targets51\\JpgConverted\\AllTargets\\'
jpg_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg')]
png_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]


for jpg, png in zip(jpg_files, png_files):
    filename = jpg.split('.')[0]
    img = cv.imread(input_dir + jpg)
    mask = cv.imread(input_dir + png, 0)
   
    list_final_images = []
    images = imageExtraction(img, mask)


# print(type(images))

    # for i, image in enumerate(images):
    #     cv.imwrite(f'{DUMP_PATH} extracted_{filename}_{i}.png', image)
    #     cv.waitKey(0)
    #     cv.destroyAllWindows()

    for i, image in enumerate(list_final_images):
        cv.imwrite(f'{DUMP_PATH}{filename}_{i}.png', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
