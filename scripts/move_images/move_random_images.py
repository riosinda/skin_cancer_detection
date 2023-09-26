import random
import shutil
import os
import csv

# Function to generate random numbers
def random_nums(low, upper, n):
    num_posibles = list(range(low, upper + 1))
    random_nums = random.sample(num_posibles, n)
    return random_nums

# Function to generate file name
def file_name(folder,count):
    if folder == "melanoma":
        return f"mel_{count:05}.jpg"
    elif folder == "nevus":
        return f"nev_{count:05}.jpg"
    elif folder == "basal cell carcinoma":
        return f"bcc_{count:05}.jpg"
    elif folder == "squamous cell carcinoma":
        return f"scc_{count:05}.jpg"
    
# Function to filter files
def filter_files(files):
    path = "../../csv_files/ISCI_bad_images.csv"
    bad_images = set()
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bad_images.add(row[0])
    good_images = [file for file in files if file not in bad_images]
    return good_images


# Function to move images
def main(folders):
    for folder in folders:
        max_images = 500#Max number of images to move
        original_folder = "D:/SkinCancerDatasets/ISIC/images_separate_type/" + folder + "/"
        new_folder = "D:/SkinCancerDatasets/FinalDataset/images/" + folder + "/"
        
        if os.path.exists(new_folder):      # If folder does exist
            shutil.rmtree(new_folder)       # Delete folder
            os.makedirs(new_folder)         # Create folder
        else:
            os.makedirs(new_folder)         # Create folder

        files = os.listdir(original_folder)
        files = filter_files(files)

        if len(files) < max_images:
            max_images = len(files)
        
        random_list = random_nums(0, len(files) - 1, max_images)
        count = 0
        for i in random_list:
            shutil.copy(original_folder + files[i], new_folder + file_name(folder,count))
            print(f"Image: {count} / {max_images}",end="\r")
            count += 1
        print(f"{count} images moved of {folder}")


folders = ["melanoma", "nevus", "basal cell carcinoma", "squamous cell carcinoma"] #Name of the folders to move


if __name__ == '__main__':
    main(folders)
