# import os
# import csv
# from ImageDashboradGenerator import readXmp

# # Define the directory
# directory = 'C:\\Users\\ChNa395\\Desktop\\AllTargets'
# exts = ('.jpg','.jpeg','.png', '.tif', '.tiff', '.bmp')

# with open('C:\\Users\\ChNa395\\python\\BatchRun\\output.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['filename', 'label'])
#     for img in os.listdir(directory):
#         if img.lower().endswith(exts):
#             img_no_ext_ = os.path.splitext(os.path.basename(img))[0]
#             in_xmp = os.path.join(os.path.abspath(directory),os.path.basename(img) + ".xmp")
#             tags_node_name = "digiKam:TagsList"
#             xmp_items = []
#             if os.path.isfile(in_xmp):
#                 xmp_items = readXmp(in_xmp,tags_node_name)
#                 for item in xmp_items:
#                     if item.split('/')[0] == "Label":
#                         label = item.split('/')[-1]

#         writer.writerow([img_no_ext_, label])



# import pandas as pd
# import json

# rows = []

# with open('C:\\Users\\ChNa395\\Downloads\\DeskewedTargets_json.json') as json_file:
#     data = json.load(json_file)
#     for key in data:
#         # print(d)
#         for region in data[key]['regions']:
#             filename = key.split('.')[0]
#             label = ''
#             if (region['region_attributes']['Document'] == "1"):
#                 label = 'Document'
#             elif (region['region_attributes']['Photo'] == "1"):
#                 label = 'Photo'
#             elif (region['region_attributes']['Mixed'] == "1"):
#                 label = 'Mixed'

#             row = {
#                 'Filename': filename,
#                 'Label' : label
#             }
#             rows.append(row)


# df = pd.DataFrame(rows)
# df.to_csv('C:\\Users\\ChNa395\\python\\output.csv', index=False)



import pandas as pd
import json

rows = []

with open('C:\\Users\\ChNa395\\Downloads\\via_project_15May2024_11h15m_json.json') as json_file:
    data = json.load(json_file)
    for key in data:
        filename = key.split('.')[0]
        label = ''
        file_attributes = data[key]['file_attributes']
        print(file_attributes)
        if file_attributes['Document'] == "1":
            label = 'Document'
        elif file_attributes['Photo'] == "1":
            label = 'Photo'
        elif file_attributes['Receipt'] == "1":
            label = 'Receipt'
        elif file_attributes['Card'] == "1":
            label = 'Card'
        else:
            label = 'Unknown'

        row = { 'Filename': filename, 'Label' : label }
        rows.append(row)

df = pd.DataFrame(rows)
df.to_csv('C:\\Users\\ChNa395\\python\\DemoCsv.csv', index=False)
