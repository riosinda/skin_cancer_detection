import os
import shutil

original_folder = "D:/SkinCancerDatasets/7PointCriteria/images/"
new_folder = "D:/SkinCancerDatasets/7PointCriteria/all_images/"

folders = os.listdir(original_folder)

for folder in folders:
    files = os.listdir(original_folder + folder)
    for file in files:
        shutil.copy(original_folder + folder + "/" + file, new_folder + file)
        print("File "+ file +" copied to " + new_folder + file + ".")