#-*- coding:utf-8 -*-
import os
import random
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import chardet
import io
import sys
import numpy as np
import cv2
from math import *

g_suffix = 0

def SaltAndPepper(src,percetage):
    SP_NoiseImg=src.copy()
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(SP_NoiseNum):
        randR=np.random.randint(0,src.shape[0]-1)
        randG=np.random.randint(0,src.shape[1]-1)
        randB=np.random.randint(0,3)
        if np.random.randint(0,1)==0:
            SP_NoiseImg[randR,randG,randB]=0
        else:
            SP_NoiseImg[randR,randG,randB]=255
    return SP_NoiseImg

def addGaussianNoise(image,percetage):
    G_Noiseimg = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    G_NoiseNum=int(percetage*image.shape[0]*image.shape[1])
    for i in range(G_NoiseNum):
        temp_x = np.random.randint(0,h)
        temp_y = np.random.randint(0,w)
        G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0]
    return G_Noiseimg


def isOverLap(pos1,width1,height1,pos2,width2,height2):
    if pos1[0] + width1 > pos2[0] and pos2[0] + width2 > pos1[0] and pos1[1] + height1 > pos2[1] and pos2[1] + height2 > pos1[1]:
        return True
    else:
        return False


#初始化字体颜色概率列表
color_list = []
def load_color():
    color_list.append([0, 0, 0])
    color_list.append([0, 0, 0])
    color_list.append([255, 255, 255])
    color_list.append([255, 255, 255])
    color_list.append([255, 255, 255])
    color_list.append([255, 0, 0])
    color_list.append([0, 255, 0])
    color_list.append([0, 0, 255])

#初始化字符类型概率列表
type_list = []
def load_character_type():
    type_list.append(0)
    type_list.append(0)
    type_list.append(0)
    type_list.append(1)
    type_list.append(1)
    type_list.append(2)
    type_list.append(2)
    type_list.append(3)
    type_list.append(3)
    type_list.append(3)

#加载所使用的字体
font_list=[]
def load_font(font_dir):
    if os.path.exists(font_dir):
        for file in os.listdir(font_dir):
            file_path = os.path.join(font_dir, file)
            if os.path.exists(file_path):
                font_list.append(file_path)
    if len(font_list)<= 0:
        print('font_list is NULL')
        print(__file__, sys._getframe().f_lineno)
        exit(1)

#加载底图文件路径
image_list = []
def load_images(image_dir):
    if os.path.exists(image_dir):
        for file in os.listdir(image_dir):
            print('image path:%s'%(image_dir+file))
            image_list.append(image_dir+file)
    if len(image_list)<= 0:
        print('image_list is NULL')
        print(__file__, sys._getframe().f_lineno)
        exit(1)

#加载字符内容
text_content = []
def load_text(text_path):
    #get content num/letter/letter_upper
    text_num = ['0','1','2','3','4','5','6','7','8','9']
    text_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    text_letter_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    text_content.append(text_num)
    text_content.append(text_letter)
    text_content.append(text_letter_upper)

    #get character
    text_character = []
    if os.path.exists(text_path):
        with io.open(text_path) as f:
            for i in f:
                i = i.replace('\n', '')
                text_character.append(i)
    if len(text_character) <= 0:
        print('text_character is NULL')
        print(__file__, sys._getframe().f_lineno)
        exit(1)
    text_content.append(text_character)

#获取字体样式和大小
def get_font(font_index=-1, font_size=50):
    if len(font_list)<=0:
        print('font_list is NULL')
        print(__file__, sys._getframe().f_lineno)
        exit(1)
    if (font_index == -1):
        font_index=random.randint(0,len(font_list)-1)
    font = ImageFont.truetype(font_list[font_index], font_size)
    return font

#在底图上写字
def draw_text(image_path, index_image, texts, colors, fonts,poses, width, height):
   # print(texts,poses,colors,fonts)
    dir_path = "C:/Users/wangpu01/Desktop/generate_ocr_images/generate_image/" + str(index_image)
    global g_suffix
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    new_image_path = dir_path+"/"+str(g_suffix)+".jpg"
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    for iter in range(len(poses)):
       draw.text((poses[iter][0], poses[iter][1]), texts[iter], (colors[iter][0], colors[iter][1], colors[iter][2]), fonts[iter])
    #with open("C:/Users/wangpu01/Desktop/generate_ocr_images/generate_image/txt/" + str(
    #     g_suffix) + ".txt","w") as txt_f:
    #     for iter in range(len(poses)):
    #         draw.text((poses[iter][0], poses[iter][1]), texts[iter], (colors[iter][0], colors[iter][1], colors[iter][2]),fonts[iter])
    #         txt_f.writelines(str(poses[iter][0]) + ',' + str(poses[iter][1]) + ',' + str(poses[iter][0]+width[iter]) + ',' + str(poses[iter][1]) + ',' + str(poses[iter][0]+width[iter]) + ',' + str(
    #             poses[iter][1]+height[iter]) + ',' + str(poses[iter][0]) + ',' + str(poses[iter][1]+height[iter]) + ",1," + "#" + "\n")
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    flag = random.randint(0,3)
    #if flag == 0:
    #    img = SaltAndPepper(img,0.1)
    #elif flag == 1:
    #    img = addGaussianNoise(img, 0.1)
    if flag == 2:
        img = cv2.GaussianBlur(img, (5,5), 0);
    cv2.imwrite(new_image_path,img)
    g_suffix = g_suffix + 1
    #img.save(new_image_path)
def generage_one_image(font_type_size ,index_image):
    #获取图片及宽高
    image_path = image_list[index_image]
    img = Image.open(image_path)
    img_width, img_height = img.size

    #产生字符个数len_character
    min_len = 3
    max_len = 15
    mu = 7
    sigma = 5
    line_mu = 3
    line_sigma = 2
    min_line = 1
    max_line = 5

    line_num = int(np.random.normal(mu, sigma, 1))
    #print(len_character)
    while (min_line > line_num or line_num > max_line):
        line_num = int(np.random.normal(line_mu, line_sigma, 1))
    colors =[]
    fonts = []
    poses = []
    texts = []
    width = []
    height = []
    for line in range(line_num):
        # 获取字体颜色
        color = color_list[random.randint(0, len(color_list) - 1)]
        colors.append(color)

        len_character = int(np.random.normal(mu, sigma, 1))
        while (min_len > len_character or len_character > max_len):
            len_character = int(np.random.normal(mu, sigma, 1))
        # 字体大小font_size
        max_width = int(img_width / len_character)
        max_height = img_height
        max_size = min(max_width, max_height, 300)
        min_size = 20
        if (min_size > max_size):
            return
            #print("0*********")
        font_size = random.randint(min_size, max_size)
        #获取字体位置
        scale_width = img_width-font_size*len_character
        scale_height = img_height-font_size
        x = random.randint(0,scale_width)
        y = random.randint(0,scale_height)
        pos=[x,y]
        sum_IOL = 0
        if len(poses)>0:
            count = 0
            while(count < len(poses)):
                if(sum_IOL > 20):
                    return
                if isOverLap(pos,font_size*len_character,font_size,poses[count],width[count],height[count]):
                    len_character = int(np.random.normal(mu, sigma, 1))
                    while (min_len > len_character or len_character > max_len):
                        len_character = int(np.random.normal(mu, sigma, 1))
                    max_width = int(img_width / len_character)
                    max_height = img_height
                    max_size = min(max_width, max_height, 300)
                    min_size = 20
                    if (min_size > max_size):
                       return
                    font_size = random.randint(min_size, max_size)
                    # 获取字体位置
                    scale_width = img_width - font_size * len_character
                    scale_height = img_height - font_size
                    x = random.randint(0, scale_width)
                    y = random.randint(0, scale_height)
                    pos = [x, y]
                    count = 0
                else:
                    count = count + 1
                sum_IOL = sum_IOL + 1
        poses.append(pos)
        width.append(font_size*len_character)
        height.append(font_size)
        #获取字符类型和内容
        type_index = type_list[random.randint(0,len(type_list)-1)]
        character_list = text_content[type_index]
        character_num = len(character_list)
        content = []
        for i in range(len_character):
            character_index = random.randint(0,character_num-1)
            content.append(text_content[type_index][character_index])
        text = ''.join(content)
        texts.append(text)
        index_font = random.randint(0,23)
        font = get_font(font_index=index_font, font_size=font_size)
        fonts.append(font)
    draw_text(image_path, index_image, texts,colors, fonts, poses, width, height)


def main():

    #load color probability table
    load_color()
    print("color:",len(color_list))

    #load character type probability table
    load_character_type()

    #load font
    font_path = "C:/Users/wangpu01/Desktop/generate_ocr_images/font"
    load_font(font_path)
    print("font:",font_list)
    #load image list
    image_path = "C:/Users/wangpu01/Desktop/generate_ocr_images/clean_bk_images/"
    load_images(image_path)
    #print("image:",len(image_list))
    #set text content
    text_character_path = "C:/Users/wangpu01/Desktop/generate_ocr_images/text_character.txt"
    load_text(text_character_path)
    #print("text:",text_content)
    #set text properties
    count = 0
    generage_sum = 10
    #字体逐一遍历. color红绿蓝逐一遍历. 底图逐一遍历. 字符长度3~15随机选取. 字符类型按照1:1:1:10
    for p_image in range(0, len(image_list)-1, 1):
        for p_gen in range(generage_sum):
            generage_one_image(len(font_list),p_image)
            print("{}/{}".format(count,len(image_list)*generage_sum))
            count = count + 1


if __name__ == '__main__':
    main()
