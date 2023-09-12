import cv2
import numpy as np
import os


path = "D:/SkinCancerDatasets/ISIC/images_original/"
files = os.listdir(path)

max_width = 0
max_height = 0
cont = 1
num_files = len(files)
for file in files:
    image = cv2.imread(path + file)
    height, width, channels = image.shape
    #print(f"Image {file} has width {width} and height {height}",end="\r")
    if width > max_width:
        max_width = width
    if height > max_height:
        max_height = height
    print(f"Image {cont}/{num_files}, max_width:{max_width}, max_height:{max_height}")
    cont += 1

print(f"\nMax width: {max_width}")
print(f"Max height: {max_height}")