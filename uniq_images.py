import os
import os.path
import shutil
import hashlib
import sys
from imp import reload
reload(sys)
#sys.setdefaultencoding('utf-8')

def walkDir(rootdir):
    filenames = []
    for i in os.listdir(rootdir):
        if os.path.isfile(os.path.join(rootdir, i)):
            if (i.endswith("jpg") or i.endswith("png") or i.endswith("bmp")):
                filenames.append(i)
    return filenames

def uniq_images(rootdir):
    names = walkDir(rootdir)
    if not os.path.exists(os.path.join(rootdir,"backup")):
        os.mkdir(os.path.join(rootdir,"backup"))
    desrootpath = os.path.join(rootdir,"backup")
    delnum = 0
    md5_dict = {}
    logfile = open(os.path.join(desrootpath, "recover_cmd_log.txt"), "w")
    for name in names:
        imgpath = os.path.join(rootdir, name)
        md5file = open(imgpath, "rb")

        md5 = hashlib.md5(md5file.read()).hexdigest()
        md5file.close()
        #if md5_dict.has_key(md5):
        if md5 in md5_dict:
            srcpath = imgpath
            despath = os.path.join(desrootpath, name)
            shutil.copy(srcpath, despath)
            os.remove(srcpath)
            delnum += 1
            print("repeated image: "+name)
            logfile.write("cp "+md5_dict[md5]+" "+srcpath+"\n")
        else:
            md5_dict[md5] = imgpath
    logfile.close()
    return delnum,len(names)

[delnum,number] = uniq_images("D:\\datasets\\ad_0917\\ad\\0918big")
print("total image: %d, delete number: %d\n"%(number,delnum))
