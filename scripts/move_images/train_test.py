import random
import shutil
import os

# Function to generate random numbers
def random_train(low, upper, n):
    num_posibles = list(range(low, upper + 1))
    random_nums = random.sample(num_posibles, n)
    return random_nums

def random_test(files, random_train):
    test_files = []
    for i in range(len(files)):
        if i not in random_train:
            test_files.append(i)
    return test_files

def create_folder(path):
    if os.path.exists(path):      # If folder does exist
        shutil.rmtree(path)       # Delete folder
        os.makedirs(path)         # Create folder
    else:
        os.makedirs(path)         # Create folder

path = "D:/SkinCancerDatasets/FinalDataset/images/"
folders = os.listdir(path)

for folder in folders:
    length = len(os.listdir(path + folder))
    train = int(length * 0.7)
    test = length - train

    print(f"\nFolder: {folder} - Train: {train} - Test: {test}")
    
    original_folder = path + folder + "/"
    
    train_folder = "D:/SkinCancerDatasets/FinalDataset/train/" + folder + "/"
    test_folder = "D:/SkinCancerDatasets/FinalDataset/test/" + folder + "/"
    
    create_folder(train_folder)
    create_folder(test_folder)
    
    files = os.listdir(original_folder)

    train_files = random_train(0, len(files) - 1, train)
    
    cout = 0
    for i in train_files:
        shutil.copy(original_folder + files[i], train_folder + files[i])
        print(f"Image: {cout} / {train}",end="\r")
        cout += 1
    print(f"{cout} train images moved of {folder}")
    
    test_files = random_test(files, train_files)
    cont = 0
    for i in test_files:
        shutil.copy(original_folder + files[i], test_folder + files[i])
        print(f"Image: {cont} / {test}",end="\r")
        cont += 1
    print(f"{cont} test images moved of {folder}")
