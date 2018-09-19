import os
import numpy as np
import json
import shutil
import cv2

input_root = 'C:/Users/wangpu01/Desktop/datasets/normal/'
clean_root = 'C:/Users/wangpu01/Desktop/error/normal_error/'
backup_root = 'C:/Users/wangpu01/Desktop/backup/'

def read_image_file(image_path):
    return cv2.imread(image_path)

def display(image_name, image_data):
    cv2.imshow('images', image_data)

def get_fileslist(path,files):
    fileslist = os.listdir(path)

    for filename in fileslist:
        filepath = os.path.join(path, filename)
        filepath.replace('/', '\\')
        if os.path.isdir(filepath):
            get_fileslist(filepath,files)
        else:
            files.append(filepath)
    return files


input_files = get_fileslist(input_root,[])
clean_files = get_fileslist(clean_root,[])
#IMG = cv2.imread('C:/Users/wangpu01/Desktop/error/big_error\complex_poster\0_0023753_20170324_230355.jpg')
#cv2.imshow('images',IMG)
#cv2.waitKey(0)
for iter,clean_name in enumerate(clean_files):
    clean_name,_ = os.path.splitext(clean_name)
    clean_path = os.path.join(input_root, clean_name)
    image_data = read_image_file(clean_path + '.jpg')
    #print(clean_path)
    for input_name in input_files:
        input_name, _ = os.path.splitext(input_name)
        _, name1 = os.path.split(clean_name)
        _, name2 = os.path.split(input_name)
        if name1 == name2:
            input_path = os.path.join(input_root, input_name)
            try:
                display(clean_name, image_data)
            except:
                continue
            key = cv2.waitKey(0)
            if key == ord('m'):
                shutil.move(input_path  + '.jpg',backup_root + name2 + '.jpg')
            elif key == 27:
                print("go to relax!!!")
                break