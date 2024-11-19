import json
import yaml

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


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
            json_file.write(json.dumps(data[i], indent=configuration_variables['json']['space_between_rows']))


def create_report_files(data):
    file_number = configuration_variables['files']['first_file']
    for index in range(configuration_variables['rows']['first'], count_data_rows(data),
                       configuration_variables['rows']['max']):
        json_path = f"{configuration_variables['json']['path']['file']}_{file_number}"
        write_to_json(json_path, data, index, index + configuration_variables['rows']['max'])
        file_number += configuration_variables['files']['next_file']
