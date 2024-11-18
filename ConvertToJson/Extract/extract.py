import csv
import yaml

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def convert_rows_to_dictionary(csv_reader):
    data = {}
    counter = configuration_variables['rows']['first_row']
    for row in csv_reader:
        key = counter
        counter += configuration_variables['rows']['next_row']
        data[key] = row

    return data


def open_csv_file_to_get_data(csv_path):
    with open(csv_path, encoding=configuration_variables['encode']['eight_bit']) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = convert_rows_to_dictionary(csv_reader)

    return data
