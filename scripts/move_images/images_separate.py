import csv
import os
import shutil

def move_images_from_csv(csv_file, destination_folder, origin_images):
    with open(csv_file, 'r') as file:                               # Read csv file
            reader = csv.DictReader(file)                           
            for row in reader:                                    # Iterate through rows
                image_id = row['isic_id']                         # Get image id
                diagnosis = row['benign_malignant']               # Get diagnosis
                
                if diagnosis == '':                               # If diagnosis is empty
                    diagnosis = 'unknown'
                source_image =origin_images + image_id + '.jpg'   # Get image path
                diagnosis_folder = os.path.join(destination_folder, diagnosis)  # Get destination folder
                if not os.path.exists(diagnosis_folder):      # If folder does not exist
                    os.makedirs(diagnosis_folder)
                
                shutil.move(source_image, diagnosis_folder)     # Move image to folder
                print(f"Image {source_image} moved to folder {diagnosis_folder}")

csv_file = "../../csv_files/metadata_clean.csv"             # Input csv file
origin_images = "D:/SkinCancerDatasets/ISIC/images/"        # Input images
destination_folder = "D:/SkinCancerDatasets/ISIC/images_separate_benign_malignant/"         # Output folder

move_images_from_csv(csv_file, destination_folder, origin_images)