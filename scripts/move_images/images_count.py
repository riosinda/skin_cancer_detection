import os
import csv

def count_files_per_folder(directory):                  # Count number of files per folder
    file_count_per_folder = {}

    for item in os.listdir(directory):                  # Iterate through folders
        full_path = os.path.join(directory, item)

    if os.path.isdir(full_path):                        # Check if item is a folder
            # Count number of files in folder
            num_files = len([filename for filename in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, filename))])
            file_count_per_folder[item] = num_files     # Add folder and number of files to dictionary

    return file_count_per_folder

def save_results_to_csv(counts, filename):              # Save results to csv file
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Folder', 'Number of Files'])

        for folder, num_files in counts.items():        # Iterate through dictionary
            csv_writer.writerow([folder, num_files])


directory = 'D:/SkinCancerDatasets/ISIC/images_separate_type/'      # Input directory
counts = count_files_per_folder(directory)

csv_filename = '../../csv_files/diagnosis_count.csv'    # Output csv file
save_results_to_csv(counts, csv_filename)
