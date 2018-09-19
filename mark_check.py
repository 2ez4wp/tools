import os
import numpy as np

import json
#from matplotlib import pyplot as plt
import shutil
import cv2
import matplotlib.pyplot as plt

#images_root = 'C:/Users/wangpu01/Desktop/text_line_detect/text_line_detect/imgs'
#labels_root = 'C:/Users/wangpu01/Desktop/text_line_detect/text_line_detect/output'
labels_root = 'C:/Users/wangpu01/Desktop/ocr_pr_calculate/ocr_pr_calculate/txt_aug_906_348'
images_root = 'C:/Users/wangpu01/Desktop/ocr_pr_calculate/ocr_pr_calculate/img_aug_348'
errors_root = 'C:/Users/wangpu01/Desktop/ocr_pr_calculate/ocr_pr_calculate/bak'

def display(image_data,boxes):
    #current_axis = plt.gca()
    for iter,box in enumerate(boxes):
        box = np.array(box)
        #print(np.shape(box))
        box=box.reshape((-1,1,2))
        #print(np.shape(box))
        if  iter%3 ==0:
            cv2.polylines(image_data, [box],True,(255,0,0), 3)
        if  iter%3 ==1:
            cv2.polylines(image_data, [box],True,(0,255,0), 3)
        if  iter%3 ==2:
            cv2.polylines(image_data, [box],True,(0,255,255),3)
        #current_axis.add_patch(plt.Polygon(box,color='red',fill=False, linewidth=3))
    img = cv2.resize(image_data,(600,600))
    cv2.imshow('name',img)

images_list = os.listdir(images_root)
labels_list = os.listdir(labels_root)
#print(len(images_list))
sum = 0
mv_count = 0
loss_count = 0
images_list = images_list[100:]
for image_name in images_list:
    #print(image_name)
    image_path = os.path.join(images_root,image_name)
    #image_path = "C:/Users/wangpu01/Desktop/ocr_pr_calculate/ocr_pr_calculatetxt_aug_906_348/2(335).jpg"
    image_data = cv2.imread(image_path)
    filename = image_name[0:image_name.rfind(".")]
    label_path = os.path.join(labels_root,filename+".txt")
    #if not os.path.exists(label_path):
    #    loss_count = loss_count+1
        #os.remove(image_path)
    #    new_image_path = os.path.join(errors_root, filename + '.jpg')
        #shutil.move(image_path, new_image_path)
        #print(loss_count)
    #    continue
    with open(label_path,"r") as load_f:
        boxes = []
        labels = load_f.readlines()
        load_f.close()
        for label in labels:
            label = label.split(',')
            boxTmp = label[:8]
            box = [int(i) for i in boxTmp]
            boxes.append(box)
            cv2.circle(image_data, (box[0],box[1]), 8, (0, 0, 0),-1)
        print(boxes)
        try:
            display(image_data, boxes)
        except:
            continue

        key = cv2.waitKey(0)
        if key == 27:
             print("go to relax!!!")
             break
        elif key == 100:
            #os.remove(label_path + '.json')
            new_image_path = os.path.join(errors_root,filename+'.jpg')
            new_json_path = os.path.join(errors_root,filename+'.txt')
            shutil.move(image_path, new_image_path)
            shutil.move(label_path, new_json_path)
            mv_count = mv_count + 1
        sum = sum  + 1
        #print("Name:%s, Sum:%d, Mv_count:%d, Loss_count:%d "%(filename + ".jpg",sum,mv_count,loss_count))

cv2.destroyAllWindows()

