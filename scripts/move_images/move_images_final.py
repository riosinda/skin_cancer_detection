import random
import shutil
import os
import csv

class MoveImages:
    # Function to generate file name
    
    def exist_folder(self,folder):
        if os.path.exists(folder):      # If folder does exist
            shutil.rmtree(folder)       # Delete folder
            os.makedirs(folder)         # Create folder
        else:
            os.makedirs(folder)         # Create folder

    def file_name(self,folder):
        if folder == "melanoma/":
            self.mel_count += 1

            if self.mel_count == 0:
                self.exist_folder(self.new_folder)

            namefile = f"mel_{self.mel_count:05}.jpg"
            return namefile
        
        elif folder == "nevus/":
            self.nev_count += 1

            if self.nev_count == 0:
                self.exist_folder(self.new_folder)

            namefile = f"nev_{self.nev_count:05}.jpg"
            return namefile
        
        elif folder == "basal cell carcinoma/":
            self.bcc_count += 1
            
            if self.bcc_count == 0:
                self.exist_folder(self.new_folder)

            namefile = f"bcc_{self.bcc_count :05}.jpg"
            return namefile
        
        elif folder == "squamous cell carcinoma/":
            self.scc_count += 1

            if self.scc_count == 0:
                self.exist_folder(self.new_folder)

            namefile = f"scc_{self.scc_count:05}.jpg"
            return namefile
    
    # Function to filter files
    def filter_files(self,files):
        path = "../../csv_files/ISCI_bad_images.csv"
        bad_images = set()

        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                bad_images.add(row[0])
        good_images = [file for file in files if file not in bad_images]
        
        return good_images

    def __init__(self):
        datasets = ["ISIC/separate_type/", "7PointCriteria/separate_type/", "PAD-UFES-20/separate_type/"]
        folders = ["basal cell carcinoma/", "squamous cell carcinoma/"]
        
        datasets_path = "D:/SkinCancerDatasets/"
        new_path = "D:/SkinCancerDatasets/images_dataset/images/"
        
        self.mel_count = -1
        self.nev_count = -1
        self.bcc_count = -1
        self.scc_count = -1
        
        for dataset in datasets:
            print(" ")
            print(dataset)

            for folder in folders:
                num_images = 50000 #Max number of images to move per folder
                original_folder = datasets_path + dataset + folder
                self.new_folder = new_path + folder
                
                try:

                    files = os.listdir(original_folder)
                    files = self.filter_files(files)

                    if len(files) < num_images:
                        num_images = len(files)
                    count = 0
                    for i in range(num_images):
                        count += 1
                        name = self.file_name(folder)
                        shutil.copy(original_folder + files[i], self.new_folder + name)
                        print(f"Image: {count} / {num_images}",end="\r")

                    print(f"{count} images moved of {folder}")
                
                except FileNotFoundError:
                    print("Folder not found")
                    pass

if __name__ == '__main__':
    move = MoveImages()