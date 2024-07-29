import os
import csv
import re
from datetime import datetime

def sanitize_fieldname(fieldname):
    return re.sub(r'[^\w\-_]', '_', fieldname)

def sanitize_value(value):
    date_formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d"
    ]
    for fmt in date_formats:
        try:
            date = datetime.strptime(value, fmt)
            return "ISODate('{}')".format(date.isoformat())
        except ValueError:
            pass
    
    value = value.strip().strip('"')
    
    if value.replace('.', '').isdigit():
        return value
    
    return "'{}'".format(value.replace("'", "\\'"))

def process_csv_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for _ in range(14):
            next(reader, None)

        header = next(reader)
        sanitized_header = [sanitize_fieldname(field) for field in header]
        writer.writerow(sanitized_header)

        for row in reader:
            sanitized_row = [sanitize_value(value) for value in row]
            writer.writerow(sanitized_row)

def main():
    for filename in os.listdir('.'):
        if filename.endswith('.csv'):
            input_file = filename
            output_file = "sanitized_{}".format(filename)
            process_csv_file(input_file, output_file)
            print("Processed {} -> {}".format(input_file, output_file))

if __name__ == "__main__":
    main()
