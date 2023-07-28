import csv

def delte_rows(int_file, out_file):
    rows = []

    with open(int_file, 'r') as csv_file:
        csv = csv.reader(csv_file)
        for row in csv:
            rows.append(row)

    rows_filters = [row for row in rows if any(row)]

    with open(out_file, 'w', newline='') as csv_file:
        write_csv = csv.writer(csv_file)
        write_csv.writerows(rows_filters)

int_file = '../../csv_files/metadata.csv'
out_file = '../../csv_files/metadata_clean.csv'
delte_rows(int_file, out_file)
