import csv
import os
import shutil

def move_images_from_csv(csv_file, destination_folder, origin_images):
    with open(csv_file, 'r') as file:                               # Read csv file
            reader = csv.DictReader(file)       
            print(reader.fieldnames)                    #
            for row in reader:                                    # Iterate through rows
                image_id = row['img_id']                         # Get image id
                diagnosis = row['diagnostic']               # Get diagnosis
                
                if diagnosis == '':                               # If diagnosis is empty
                    diagnosis = 'unknown'
                source_image =origin_images + image_id #+ '.jpg'   # Get image path
                diagnosis_folder = os.path.join(destination_folder, diagnosis)  # Get destination folder
                if not os.path.exists(diagnosis_folder):      # If folder does not exist
                    os.makedirs(diagnosis_folder)
                
                shutil.copy(source_image, diagnosis_folder)     # Move image to folder
                print(f"Image {source_image} moved to folder {diagnosis_folder}")

csv_file = "../../csv_files/metadata/PADUFES20_metadata.csv"             # Input csv file
origin_images = "D:/SkinCancerDatasets/PAD-UFES-20/images/"        # Input images
destination_folder = "D:/SkinCancerDatasets/PAD-UFES-20/separate_diagnosis/"         # Output folder

move_images_from_csv(csv_file, destination_folder, origin_images)