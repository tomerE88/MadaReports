import csv
import json
import os
import yaml

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def open_csv_file_to_get_data(csv_path):
    with open(csv_path, encoding=configuration_variables['encode']['eight_bit']) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = convert_rows_to_dictionary(csv_reader)

    return data


def convert_rows_to_dictionary(csv_reader):
    data = {}
    for row in csv_reader:
        key = row[configuration_variables['json']['key']]
        data[key] = row

    return data


def count_data_rows(data):
    return len(data)


def write_to_json(json_path, data):
    with open(json_path, configuration_variables['files']['write'],
              encoding=configuration_variables['encode']['eight_bit']) as json_file:
        json_file.write(json.dumps(data, indent=configuration_variables['json']['space_between_rows']))


def create_folder(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists")


def main():
    json_path = r'mada_reports_jsons'
    json_file = f'{json_path}/mada_report1.json'
    csv_path = r'C:\Users\storm\PycharmProjects\myProjects\MadaReportss\MadaReports - MadaReports.csv'

    create_folder(json_path)
    data = open_csv_file_to_get_data(csv_path)
    write_to_json(json_file, data)


if __name__ == '__main__':
    main()
