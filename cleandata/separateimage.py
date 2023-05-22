import csv
import os
import shutil

def move_images_from_csv(csv_file, destination_folder, origin_images):
    with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                image_id = row['image_id']
                dx = row['dx']
                source_image =origin_images + image_id + '.jpg'
                dx_folder = os.path.join(destination_folder, dx)
                if not os.path.exists(dx_folder):
                    os.makedirs(dx_folder)
                
                shutil.move(source_image, dx_folder)
                print(f"Image {source_image} moved to folder {dx_folder}")

# Usage example
csv_file = "D:/dataset/HAM10000_metadata.csv"
destination_folder = "D:/dataset/image_separate/"
origin_images = "D:/dataset/HAM10000_images_part_1/"

move_images_from_csv(csv_file, destination_folder, origin_images)
