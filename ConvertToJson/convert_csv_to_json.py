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
    counter = configuration_variables['rows']['first_row']
    for row in csv_reader:
        key = counter
        counter += configuration_variables['rows']['next_row']
        data[key] = row

    return data


def count_data_rows(data):
    return len(data)


def check_maximum_rows(data):
    num_rows = count_data_rows(data)
    return True if num_rows <= configuration_variables['rows']['max'] else False


def write_to_json(json_path, data, index_min, index_max):
    with open(json_path, configuration_variables['files']['write'],
              encoding=configuration_variables['encode']['eight_bit']) as json_file:

        if index_max > count_data_rows(data):
            index_max = count_data_rows(data)

        for i in range(index_min, index_max):
            print(i)
            print(json_path)
            json_file.write(json.dumps(data[i], indent=configuration_variables['json']['space_between_rows']))


def create_folder(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists")


def main():
    csv_path = r'C:\Users\storm\PycharmProjects\myProjects\MadaReportss\MadaReports - MadaReports.csv'

    create_folder(configuration_variables['json']['path']['folder'])
    data = open_csv_file_to_get_data(csv_path)
    file_number = configuration_variables['files']['first_file']
    if check_maximum_rows(data):
        json_path = f"{configuration_variables['json']['path']['file']}_{file_number}"
        write_to_json(json_path, data, configuration_variables['rows']['first'], configuration_variables['rows']['max'])
    else:
        for index in range(configuration_variables['rows']['first'], count_data_rows(data),
                           configuration_variables['rows']['max']):
            json_path = f"{configuration_variables['json']['path']['file']}_{file_number}"
            write_to_json(json_path, data, index, index + configuration_variables['rows']['max'])
            file_number += configuration_variables['files']['next_file']


if __name__ == '__main__':
    main()
