import csv

def delte_rows(int_file, out_file):         # Delete empty rows from csv file
    rows = []

    with open(int_file, 'r') as csv_file:   # Read csv file
        csv = csv.reader(csv_file)
        for row in csv:                     # Append rows to list
            rows.append(row)

    rows_filters = [row for row in rows if any(row)]    # Delete empty rows

    with open(out_file, 'w', newline='') as csv_file:   # Write csv file
        write_csv = csv.writer(csv_file)
        write_csv.writerows(rows_filters)               # Write rows to csv file

int_file = '../../csv_files/metadata.csv'           # Input file
out_file = '../../csv_files/metadata_clean.csv'     # Output file
delte_rows(int_file, out_file)
