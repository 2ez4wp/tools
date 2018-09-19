import os
import shutil
root =  "D:\\datasets\\ad_0917\\0918\\"

list_1 = ["first_poster","first_big","after2_big","after2_poster","after1_big","after1_slogo","after1_clogo","after1_sposter","after1_cposter","after1_mnist"]
list_2 = ['big','room','house','cert','norm','sposter','cposter','slogo','clogo','mnist']
dst_root = "D:\\datasets\\ad_0917\\0918"

def rename(root):
    global count
    for root_1 in list_1:
        for root_2 in list_2:
            path = root + root_1 + "\\" + root_2
            if os.path.exists(path):
                for file in os.listdir(path):
                    (filepath, tempfilename) = os.path.split(file)
                    (prename, extension) = os.path.splitext(tempfilename)
                    name = prename + "_" + str(count)
                    print("file:",path,file,name)
                    count = count + 1
                    os.rename(os.path.join(path, file), os.path.join(path,name + ".jpg"))
                    if not os.path.exists(dst_root + root_2):
                        os.mkdir(dst_root + root_2)
                    shutil.move(os.path.join(path,name + ".jpg"), os.path.join(dst_root + root_2 + "\\" + name + ".jpg"))

if __name__ == "__main__":
    count = 0
    rename(root)