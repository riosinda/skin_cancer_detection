import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import shutil

def create_folder(path):
    if os.path.exists(path):      # If folder does exist
        shutil.rmtree(path)       # Delete folder
        os.makedirs(path)         # Create folder
    else:
        os.makedirs(path)         # Create folder

def resize(image, max_width, max_height):
    height, width, channels = image.shape
    if width >height:
        new_width = max_width
        new_height = int(height * (new_width / width))
    else:
        new_height = max_height
        new_width = int(width * (new_height / height))
    
    resized_img = cv2.resize(image, dsize=(new_width, new_height), interpolation=cv2.INTER_CUBIC)
    return resized_img

def comprobation_resize(image, max_width, max_height):
    height, width, channels = image.shape
    if width <max_width:
        black = np.zeros((height,max_width-width,channels),dtype=np.uint8)
        image = np.concatenate((image,black),axis=1)
    if height <max_height:
        black = np.zeros((max_height-height,width,channels),dtype=np.uint8)
        image = np.concatenate((image,black),axis=0)
    return image

def main(folders, max_width, max_height):
    for folder in folders:
        print(f"Moving and resizing images of {folder}...")
        path = "D:/SkinCancerDatasets/dataset/images/" + folder + "/"
        new_path = "D:/SkinCancerDatasets/dataset/images/resized/" + folder + "/"
        create_folder(new_path)
        files = os.listdir(path)

        cont = 1
        for file in files:
            image = cv2.imread(path + file)
            height, width, channels = image.shape
            
            resized_img = resize(image, max_width, max_height)
            height, width, channels = resized_img.shape
            if width < max_width:
                black = np.zeros((height,int((max_width-width)/2),channels),dtype=np.uint8)
                resized_img = np.concatenate((resized_img,black),axis=1)
                resized_img = np.concatenate((black,resized_img),axis=1)
            
            if height < max_height:
                black = np.zeros((int((max_height-height)/2),max_width,channels),dtype=np.uint8)
                resized_img = np.concatenate((resized_img,black),axis=0)
                resized_img = np.concatenate((black,resized_img),axis=0)
            
            resized_img = comprobation_resize(resized_img, max_width, max_height)
            
            print(f"Image {cont}/{len(files)} resized",end="\r")
            cv2.imwrite(new_path + file, resized_img)
            cont += 1

max_width = 224
max_height = 224

folders = ["melanoma", "nevus", "basal cell carcinoma", "squamous cell carcinoma"]

if __name__ == "__main__":
    main(folders, max_width, max_height)