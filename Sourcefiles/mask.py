import numpy as np
import cv2 as cv
import json

def create_mask(shape,polygon_x,polygon_y):
    mask_img = np.zeros((shape[0],shape[1]),np.uint8)
    polygon_x = np.asarray(polygon_x,np.int32).reshape((len(polygon_x),1))
    polygon_y = np.asarray(polygon_y,np.int32).reshape((len(polygon_y),1))
    polygon = np.hstack((polygon_x,polygon_y))
    mask_img = cv.fillPoly(mask_img,[np.int32(polygon)],255)
    return mask_img


with open('C:\\Users\\ChNa395\\Downloads\\AllTargets_json.json') as json_file:
    data = json.load(json_file)
    i = 0
    for key in data:
        mask = np.zeros((3909,2550), np.uint8)
        filename = data[key]['filename']
        filename = filename.split('.')[0]
        for region in data[key]['regions']:
            att1 = region['shape_attributes']['all_points_x']
            att2 = region['shape_attributes']['all_points_y']
            # mask = create_mask_img((2550,3909),att1,att2)
            region_mask = create_mask((3909,2550),att1,att2)
            mask = cv.bitwise_or(mask, region_mask)
        cv.imwrite(f'C:\\Users\\ChNa395\\Desktop\\Targets51\\JpgConverted\\AllTargets\\{filename}.png', mask)
        i += 1

# mask = create_mask_img((2550,3909),[407,534,429,315,183,78,43],[41,65,419,447,383,477,478])
# # cv.imshow("Image Mask", mask)
cv.waitKey(0)