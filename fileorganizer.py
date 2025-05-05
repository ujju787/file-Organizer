import os 
import shutil
#this is for input path of the folder/file where organization to be done
path=input("enter the path to organize :")
files=os.listdir(path) 
count=0

for file in files:
    filename,extension=os.path.splitext(file)
    extension=extension[1:]
    if os.path.exists(path+ '/'+extension):
        shutil.move(path+ '/' +file, path+'/'+extension+'/'+file)#moving file to  existing directory
        count+=1
       
    else:
        os.makedirs(path+'/'+extension) #creating directory 
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)# moving files to newly created directory
        count+=1
        
print(" all file are  organized")
print("loop count for organizing : "  + count )