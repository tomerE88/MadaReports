import json
import yaml

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def count_data_rows(data):
    return len(data)


def write_to_json(json_path, data, index_min, index_max):
    with open(json_path, configuration_variables['files']['write'],
              encoding=configuration_variables['encode']['eight_bit']) as json_file:

        if index_max > count_data_rows(data):
            index_max = count_data_rows(data)

        for i in range(index_min, index_max):
            print(i)
            print(json_path)
            json_file.write(json.dumps(data[i], indent=configuration_variables['json']['space_between_rows']))
