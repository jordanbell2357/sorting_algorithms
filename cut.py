# cut.py

import csv

INPUT_FILE_PATH = 'name.basics.tsv'
OUTPUT_FILE_PATH = 'name.fields.tsv'
FIELDS = [1]

with open(INPUT_FILE_PATH, 'r') as input_file:
    csv_reader = csv.reader(input_file, delimiter='\t')
    with open(OUTPUT_FILE_PATH, 'w') as output_file:
        csv_writer = csv.writer(output_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            output_row = []
            for field in FIELDS:
                output_row.append(row[field])
            csv_writer.writerow(output_row)