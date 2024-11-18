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
    counter = 0
    for row in csv_reader:
        key = counter
        counter += 1
        data[key] = row

    return data


def count_data_rows(data):
    return len(data)


def check_maximum_rows(data):
    num_rows = count_data_rows(data)
    return True if num_rows <= configuration_variables['rows']['max'] else False


def write_to_json(json_path, data, index):
    with open(json_path, configuration_variables['files']['write'],
              encoding=configuration_variables['encode']['eight_bit']) as json_file:
        if index == configuration_variables['rows']['max']:
            return
        if index < configuration_variables['rows']['max']:
            small_index = index
            index = configuration_variables['rows']['max']
        else:
            small_index = index - configuration_variables['rows']['max']
        for i in range(small_index, index):
            print(i)
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
    if check_maximum_rows(data):
        write_to_json(configuration_variables['json']['path']['file'], data, 0)
    else:
        for index in range(0, count_data_rows(data), configuration_variables['rows']['max']):
            write_to_json(configuration_variables['json']['path']['file'], data, index)

        write_to_json(configuration_variables['json']['path']['file'], data,
                      count_data_rows(data) - configuration_variables['rows']['max'])


if __name__ == '__main__':
    main()
