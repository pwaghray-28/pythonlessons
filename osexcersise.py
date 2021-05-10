import os
print(os.getcwd())
#os.mkdir("Hello")
import shutil
path = input("Enter the folder")
listoffiles = os.listdir(path)
for file in listoffiles:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == " ":
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
