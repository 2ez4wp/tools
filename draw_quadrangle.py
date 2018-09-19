'''
description:draw quadrangle on image. firstly, read coordinate information of quadrangle from text file. then open the corresponding
image and draw the quadrangle on image.

input:
textdir:the directory which contains sevaral text file,each txt file contain sevaral quadrangle information of one image
imgdir:the directory which contains sevaral images.
output:
new_imagedir:the directory which saves the images which are drawed quadrangle
author:duanshengye@58ganji.com
'''

#encoding:utf-8
import cv2
import sys
import os
#import tensorflow as tf

#get all file path of the directory
def listdir(path, list_name):
    for file in os.listdir(path):
        if file[len(file)-4:len(file)] == '.txt':
            #file_path = os.path.join(path, file)
            list_name.append(file)

#parse txt file
def parse_txtfile(path):
    quadrangles = []
    with open(path) as f:
        for line in f.readlines():
            line = line.replace('\n','')
            points = line.split(',')
            #print(points)
            quadrangles.append(points)
        #input()
    #print(quadrangles)
    return quadrangles

#set path
print ('set path')
# textdir = 'D:/work/0-OCR/data/icdar2017/txt/'
# imgdir = 'D:/work/0-OCR/data/icdar2017/images/'
# new_imagedir = 'D:/work/0-OCR/data/icdar2017/draw/'

# textdir = 'D:/work/0-OCR/data/58-20180823/txt/'
# imgdir = 'D:/work/0-OCR/data/58-20180823/images/'
# new_imagedir = 'D:/work/0-OCR/data/58-20180823/draw/'

textdir = 'E:\\dataset\\OCR\\marked\\detect-testset\\txt_det\\'
imgdir = 'E:\\dataset\\OCR\\marked\\detect-testset\\img\\'
new_imagedir = 'E:\\dataset\\OCR\\marked\\detect-testset\\img_draw\\'

#get filelist
print('get filelist')
text_filename = []
listdir(textdir, text_filename)

#operate each textfile
print('operate each textfile')
for filename in text_filename:
    #print(filename)
    imgname = filename.replace('.txt','.jpg')
    #print(imgname)
    imgpath = imgdir+imgname
    print(imgpath)
    if os.path.exists(imgpath):
        #read image
        img = cv2.imread(imgpath)
        if img is None:
            continue
        print(filename)
        #parse txt
        quadrangles = parse_txtfile(textdir+filename)
        #draw quadrangles
        for val in quadrangles:
            cv2.line(img, (int(val[0]), int(val[1])), (int(val[2]), int(val[3])), (0,0,255), 5)
            cv2.line(img, (int(val[2]), int(val[3])), (int(val[4]), int(val[5])), (0,0,255), 5)
            cv2.line(img, (int(val[4]), int(val[5])), (int(val[6]), int(val[7])), (0,0,255), 5)
            cv2.line(img, (int(val[6]), int(val[7])), (int(val[0]), int(val[1])), (0,0,255), 5)
        new_imagepath = new_imagedir+imgname
        cv2.imwrite(new_imagepath, img)
print ('final.')
