import os
import csv

folder = "D:/SkinCancerDatasets/ISIC/images_separate_diagnosis/benign/bad"
files_names = os.listdir(folder)

with open('../../csv_files/bad_images.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    for file in files_names:
        csv_writer.writerow([file])
