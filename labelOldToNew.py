import os
import re
import numpy as np
import json
import shutil
import cv2
inputs_root =  "C:/Users/wangpu01/Desktop/text_line_detect/text_line_detect/23/"
outputs_root = "C:/Users/wangpu01/Desktop/text_line_detect/text_line_detect/output/"

def read_image_file(image_path):
    return cv2.imread(image_path)


def display(image_data):
    cv2.imshow('images', image_data)
    cv2.waitKey(0)


def labelOldToNew(input_path):
    with open(input_path,'rb') as rf:
        for line in rf:
            line = line.decode("utf-8")
            newline = (re.split("/,|/;|.jpg_split_|.png_split_|_split_1_split_23_split_",line))
            #print(line)
            name = newline[0]
            pointsline = newline[1:-1]
            #print(pointsline)
            #img = read_image_file("C:/Users/wangpu01/Desktop/text_line_detect/text_line_detect/19/imgs/" + name +".jpg")
            count = 0
            #if 1==1:
            #    display(img)
            with open(outputs_root + "23_"+name + ".txt", 'w') as wf:
                while count != len(pointsline):
                    x0 = int(pointsline[count])
                    y0 = int(pointsline[count+1])
                    x1 = int(pointsline[count+2])
                    y1 = int(pointsline[count+3])
                    x_min = x0 if x0 < x1 else x1
                    x_max = x0 if x0 > x1 else x1
                    y_min = y0 if y0 < y1 else y1
                    y_max = y0 if y0 > y1 else y1
                    #list = [x_min,y_max,x_max,y_max]
                    if x_min < x_max and y_min < y_max:
                        wf.writelines(str(x_min) +','+str(y_max)+','+str(x_max)+','+str(y_max)+','+str(x_max)+','+str(y_min)+','+str(x_min)+','+str(y_min)+ ",1,"+ "#" + "\n" )
                    #pts = np.array([[x_min,y_max],[x_max,y_max],[x_max,y_min],[x_min,y_min]],np.int32)
                    #pts = pts.reshape((-1, 1, 2))
                    #img = cv2.polylines(img, [pts], True, (0, 255, 255),1)
                    count = count + 4
                #display(img)
                #print (point)
            #print(line)
            #save_data =
            #with open(outputs_root + newline[0] + ".txt", 'wb') as wf:
            #    wf.write()

if __name__ =="__main__":
    labelOldToNew(inputs_root+'desc')

