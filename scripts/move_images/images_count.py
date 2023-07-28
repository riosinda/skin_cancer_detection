import os
import csv

def count_files_per_folder(directory):
    file_count_per_folder = {}

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        if os.path.isdir(full_path):
            num_files = len([filename for filename in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, filename))])
            file_count_per_folder[item] = num_files

    return file_count_per_folder

def save_results_to_csv(counts, filename):
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Folder', 'Number of Files'])

        for folder, num_files in counts.items():
            csv_writer.writerow([folder, num_files])


directory = 'D:/SkinCancerDatasets/ISIC/images_separate_type/'
counts = count_files_per_folder(directory)

csv_filename = '../../csv_files/diagnosis_count.csv'
save_results_to_csv(counts, csv_filename)
