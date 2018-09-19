import os
import numpy as np

import json
# from matplotlib import pyplot as plt
import shutil
import cv2

datasets_root = 'C:\\Users\wangpu01\Desktop\datasets/'

big_root = datasets_root + "big/"
mnist_root = datasets_root + 'mnist/'
simple_poster_root = datasets_root + 'simple_poster/'
complex_poster_root = datasets_root + 'complex_poster/'
simple_logo_root = datasets_root + 'simple_logo/'
complex_logo_root = datasets_root + 'complex_logo/'
simple_other_root = datasets_root + 'simple_pther/'
complex_other_root = datasets_root + 'complex_other/'
other_root = datasets_root + 'other/'
input_root = datasets_root + 'tphlxfs-21080827-3196/'


def read_image_file(image_path):
    return cv2.imread(image_path)


def display(image_name, image_data):
    cv2.imshow('images', image_data)

    #if image_data.empty():
        #imshow("window", image);
    # current_axis = plt.gca()
    #input_path = os.path.join(input_root, image_name)
    #print(image_name  )
    #print (image_data.shape)
    #  img = cv2.resize(image_data, (600, 600))
    #cv2.imwrite(output_path + '.jpg', image_data)


images_list = os.listdir(input_root)
#labels_list = os.listdir(labels_root)
images_list.sort()
print(images_list[19])
# print(len(images_list))
print(images_list)
for iter,image_name in enumerate(images_list):
   #  print(iter)
    image_name, _ = os.path.splitext(image_name)
    #print(image_name)
    image_path = os.path.join(input_root, image_name)
    image_data = read_image_file(image_path + '.jpg')
    try:
        display(image_name, image_data)
    except:
        continue
    big_path =  big_root + image_name
    mnist_path = mnist_root + image_name
    simple_logo_path = simple_logo_root + image_name
    complex_logo_path = complex_logo_root + image_name
    simple_poster_path = simple_poster_root + image_name
    complex_poster_path = complex_poster_root + image_name
    simple_other_path = simple_other_root + image_name
    complex_other_path = complex_other_root + image_name
    other_path = other_root + image_name
    key = cv2.waitKey(0)
    print(image_path + '.jpg')
    if key == ord('1'):
        shutil.move(image_path + '.jpg', mnist_path + '.jpg')
    elif key == ord('2'):
        shutil.move(image_path + '.jpg', big_path + '.jpg')
    elif key == ord('3'):
        shutil.move(image_path + '.jpg', simple_logo_path + '.jpg')
    elif key == ord('4'):
        shutil.move(image_path + '.jpg', complex_logo_path + '.jpg')
    elif key == ord('5'):
        shutil.move(image_path + '.jpg', simple_poster_path + '.jpg')
    elif key == ord('6'):
        shutil.move(image_path + '.jpg', complex_poster_path + '.jpg')
    elif key == ord('7'):
        shutil.move(image_path + '.jpg', simple_other_path + '.jpg')
    elif key == ord('8'):
        shutil.move(image_path + '.jpg', complex_other_path + '.jpg')
    #elif key == ord('0'):
    #    shutil.move(image_path + '.jpg', other_path + '.jpg')
    elif key == 27:
        print("go to relax!!!")
        break
    #label_path = os.path.join(labels_root, image_name)
    #error_path = os.path.join(errors_root, image_name)
    #with open(label_path + ".json", "r") as load_f:
    #    boxes = []
    #    label = json.load(load_f)
    #    for shape in label['shapes']:
    #       box = shape['points']
            # box = np.array(box)
    #        boxes.append(box)
        # print(boxes)
    #    display(image_name, image_data, boxes)
    #    if key == 27:
    #        continue
    #    elif key == 'd':
    #        os.remove(label_path + '.json')
    #        shutil.move(image_path + '.jpg', error_path + '.jpg')
cv2.destroyAllWindows()
# continue

