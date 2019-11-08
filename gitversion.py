import os,shutil
import glob,hashlib
from colorama import Fore
flag=0

def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

while True:
    command=input(Fore.BLACK + "Enter command ")
    if(command=="git init" and flag==0):
        flag=1
        path=os.getcwd()
        path1=path+"/git/object"
        path2=path+"/git/refs"
        path3=path+"/git/index"
        try:
            os.makedirs(path1,0o777,exist_ok=False)
            os.makedirs(path2,0o777,exist_ok=False)
            os.makedirs(path3,0o777,exist_ok=False)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
    elif(command=="git status" and flag==1):
        #print("hey")  
        path=os.getcwd()
        #print(path)
        #print(glob.glob(path))
        dirs = os.listdir( path )
        for file in dirs:
            checkfile=path+"/"+file
            if(os.path.isfile(checkfile)):
                message = hash_file(file)
                checkpath=path+"/git/refs/"+message
                if(os.path.exists(checkpath)):
                    #print("yes")
                    #message1 = hash_file(file)
                   # message2 = hash_file(checkpath)
                    #if(message1==message2):
                   #     continue
                   # else :
                    print(Fore.GREEN +"Unmodified  "+file)
                    continue
                else:
                    print(Fore.RED +"Modified  "+file)
 
    elif(command=="git add ." and flag==1):
        filelist=[]
        path=os.getcwd()
        dirs = os.listdir( path )
        for file in dirs:
            checkfile=path+"/"+file
            if(os.path.isfile(checkfile)):
                message = hash_file(file)
                checkpath=path+"/git/refs/"+message
                if(os.path.exists(checkpath)):
                    continue
                else:
                    
                    try:
                        os.makedirs(checkpath,0o777,exist_ok=False)
                    except OSError:
                        print ("Creation of the directory %s failed" % path)
                    shutil.copy(file,checkpath)
                    
                    
            
    
