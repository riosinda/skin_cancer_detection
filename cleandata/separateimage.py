import csv
import os
import shutil

def move_images_from_csv(csv_file, destination_folder):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                image_id = row['image_id']
                dx = row['dx']
                source_image = image_id + '.jpg'
                dx_folder = os.path.join(destination_folder, dx)

                if not os.path.exists(dx_folder):
                    os.makedirs(dx_folder)

                shutil.move(source_image, dx_folder)
                print(f"Image {source_image} moved to folder {dx_folder}")
    except FileNotFoundError:
        print("The CSV file does not exist.")

# Usage example
csv_file = "path/to/csv/file.csv"
destination_folder = "path/to/destination/folder"

move_images_from_csv(csv_file, destination_folder)
