#encoding:utf-8
import os
#from urllib import request
import urllib, urllib3
from urllib import request
import threading

#读取url文件
f = open('D:\\docs\\after2_big.txt',"r")
lines = f.readlines()
print (len(lines))

#设置图片保存目录
dirPath = "D:\\datasets\\after2_big"


def down_image(url, image_path):
    request.urlretrieve(url, image_path)

#预处理：切分line、拼接url前缀
msg_id = 0
threhold = 430
for line in lines:
    msg_id = msg_id + 1
    if msg_id<=threhold: #最后一个msg_id重新下载
       continue
    url_list = line.split('|')
    print(line)
    #url_list = url_list[1:] #删除第一个空字符串
    url_list[len(url_list)-1] = url_list[len(url_list)-1].replace('\n','') #去掉最后一个元素中的换行符
    print ('%d %s'%(msg_id,url_list))


    #创建当前msg的目录
    #msg_dir = os.path.join(dirPath,str(msg_id))
    #print (msg_dir)
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

    #下载当前msg包含的图片
    threads=[]
    for i, url in enumerate(url_list,0):
        #拼接前缀
        print ('val:%s'%url)
        #filepath = msg_dir + "/" + str(msg_id)+"_"+str(i)+".jpg"
        filepath = dirPath + "/" + str(msg_id) + "_" + str(i) + ".jpg"
        #下载
        #urllib.urlretrieve(url, filepath)
        t = threading.Thread(target=down_image, args=(url,filepath))
        t.start()
        threads.append(t)
    for i in range(len(threads)):
        threads[i].join()