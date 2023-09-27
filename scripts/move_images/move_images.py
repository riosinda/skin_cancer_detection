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

            self.namefile = f"mel_{self.mel_count:05}.jpg"
            return self.namefile, self.mel_count
        
        elif folder == "nevus/":
            self.nev_count += 1

            if self.nev_count == 0:
                self.exist_folder(self.new_folder)

            self.namefile = f"nev_{self.nev_count:05}.jpg"
            return self.namefile, self.nev_count
        
        elif folder == "basal cell carcinoma/":
            self.bcc_count += 1
            
            if self.bcc_count == 0:
                self.exist_folder(self.new_folder)

            self.namefile = f"bcc_{self.bcc_count :05}.jpg"
            return self.namefile, self.bcc_count
        
        elif folder == "squamous cell carcinoma/":
            self.scc_count += 1

            if self.scc_count == 0:
                self.exist_folder(self.new_folder)

            self.namefile = f"scc_{self.scc_count:05}.jpg"
            return self.namefile, self.scc_count
    
    # Function to filter files
    def filter_files(self,files):
        self.path = "../../csv_files/ISCI_bad_images.csv"
        self.bad_images = set()

        with open(self.path, 'r') as file:
            self.reader = csv.reader(file)
            for row in self.reader:
                self.bad_images.add(row[0])
        self.good_images = [file for file in files if file not in self.bad_images]
        
        return self.good_images

    def __init__(self):
        self.datasets = ["ISIC/separate_type/", "7PointCriteria/separate_type/", "PAD-UFES-20/separate_type/"]
        self.folders = ["melanoma/", "nevus/", "basal cell carcinoma/", "squamous cell carcinoma/"]
        
        self.datasets_path = "D:/SkinCancerDatasets/"
        self.new_path = "D:/SkinCancerDatasets/dataset/images/"
        
        self.mel_count = -1
        self.nev_count = -1
        self.bcc_count = -1
        self.scc_count = -1
        
        for dataset in self.datasets:
            print(" ")
            print(dataset)

            for folder in self.folders:
                self.num_images = 50000 #Max number of images to move per folder
                self.original_folder = self.datasets_path + dataset + folder
                self.new_folder = self.new_path + folder
                
                try:

                    self.files = os.listdir(self.original_folder)
                    self.files = self.filter_files(self.files)

                    if len(self.files) < self.num_images:
                        self.num_images = len(self.files)
                    
                    for i in range(self.num_images):
                        name,count = self.file_name(folder)
                        shutil.copy(self.original_folder + self.files[i], self.new_folder + name)
                        print(f"Image: {count+1} / {self.num_images}",end="\r")

                    print(f"{count+1} images moved of {folder}")
                
                except FileNotFoundError:
                    print("Folder not found")
                    pass

if __name__ == '__main__':
    move = MoveImages()