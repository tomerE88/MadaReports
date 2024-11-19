import csv
import yaml
import ConvertToJson.Transform.transform as transform

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def open_csv_file_to_get_data(csv_path):
    with open(csv_path, encoding=configuration_variables['encode']['eight_bit']) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = transform.convert_rows_to_dictionary(csv_reader)
        return data
