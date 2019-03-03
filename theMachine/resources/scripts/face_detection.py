import cv2
import sys
import os



def get_file(folder,file,mode="r"):
    
    filePath = os.getcwd()+"\\resources\\%s\\%s"  %  (folder,file)

    print(filePath)
    
    f=open(filePath,mode)

    return f
    
    

def face_detection(image,faceCascade=""):
    file=get_file("requirements","face.xml")
    
