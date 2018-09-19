import os
import numpy as np
import shutil
import  random
#import cv2

input_root = 'C:/Users/wangpu01/Desktop/test_image-20180829/test_image-20180829/poster/'
output_root = 'C:/Users/wangpu01/Desktop/testdata/poster/'
def randomSelection(num):
    count = 0
    input_list = os.listdir(input_root)
    for iter,image_name in enumerate(input_list):
        image_name, _ = os.path.splitext(image_name)
        input_path = input_root + image_name
        output_path = output_root + image_name
        rd_num =  random.random()
        if rd_num > 0.5 and count < num:
            shutil.copy(input_path + '.jpg', output_path + '.jpg')
            count = count + 1

if __name__ == '__main__':
    randomSelection(5000)