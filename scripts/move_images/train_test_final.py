import random
import shutil
import os

# Function to create folders if they don't exist
def create_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    
#tipo = "mirror"
tipo = "black"
path = "D:/SkinCancerDatasets/images_dataset/resized/"+tipo+"/"
folders = os.listdir(path)

for folder in folders:
    length = len(os.listdir(path + folder))
    test = 100
    train = int((length - test) * 0.7)
    validation = length - train - test

    print(f"\nFolder {folder} -> Train: {train} - Validation: {validation} - Test: {test}")

    original_folder = path + folder + "/"
    if folder == "basal cell carcinoma":
        folder = "bcc"
    elif folder == "squamous cell carcinoma":
        folder = "scc"
        
    train_folder = "D:/SkinCancerDatasets/dataset/"+tipo +"/train/" + folder + "/"
    validation_folder = "D:/SkinCancerDatasets/dataset/"+tipo+"/validation/" + folder + "/"
    test_folder = "D:/SkinCancerDatasets/dataset/"+tipo+"/test/" + folder + "/"

    create_folder(train_folder)
    create_folder(validation_folder)
    create_folder(test_folder)

    files = os.listdir(original_folder)
    num_files = len(files)

    # Genera una lista de índices de imágenes
    image_indices = list(range(num_files))
    random.shuffle(image_indices)

    # Divide en conjuntos de entrenamiento, validación y prueba
    train_indices = image_indices[:train]
    validation_indices = image_indices[train:train + validation]
    test_indices = image_indices[train + validation:]

    # Copia las imágenes a las carpetas de destino según los conjuntos de índices
    for i in train_indices:
        shutil.copy(original_folder + files[i], train_folder + files[i])

    for i in validation_indices:
        shutil.copy(original_folder + files[i], validation_folder + files[i])

    for i in test_indices:
        shutil.copy(original_folder + files[i], test_folder + files[i])

    print(f"Images moved for {folder}: Train - {len(train_indices)}, Validation - {len(validation_indices)}, Test - {len(test_indices)}")
