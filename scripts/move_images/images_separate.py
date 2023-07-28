import csv
import os
import shutil

def move_images_from_csv(csv_file, destination_folder, origin_images):
    with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                image_id = row['isic_id']
                diagnosis = row['benign_malignant']
                
                if diagnosis == '':
                    diagnosis = 'unknown'
                source_image =origin_images + image_id + '.jpg'
                diagnosis_folder = os.path.join(destination_folder, diagnosis)
                if not os.path.exists(diagnosis_folder):
                    os.makedirs(diagnosis_folder)
                
                shutil.move(source_image, diagnosis_folder)
                print(f"Image {source_image} moved to folder {diagnosis_folder}")

csv_file = "../../csv_files/metadata_clean.csv"
origin_images = "D:/SkinCancerDatasets/ISIC/images/"
destination_folder = "D:/SkinCancerDatasets/ISIC/images_separate_benign_malignant/"

move_images_from_csv(csv_file, destination_folder, origin_images)