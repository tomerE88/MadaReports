import csv
import json
import os


def open_csv_file(csv_path):
    with open(csv_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return csv_reader


def convert_rows_to_dictionary(csv_reader):
    data = {}
    for row in csv_reader:
        key = row['IDNum']
        data[key] = row

    return data


def write_to_json(json_path, data):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))


def create_folder(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")


def main():
    csv_path = r'MadaReports - MadaReports.csv'
    json_path = r'mada_reports'

    csv_reader = open_csv_file(csv_path)
    data = convert_rows_to_dictionary(csv_reader)
    write_to_json(json_path, data)


if __name__ == '__main__':
    main()
