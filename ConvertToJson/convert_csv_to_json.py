import os
import yaml

import Extract.extract as extract
import Load.load as load

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def count_data_rows(data):
    return len(data)


def check_maximum_rows(data):
    num_rows = count_data_rows(data)
    return True if num_rows <= configuration_variables['rows']['max'] else False


def create_folder(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists")


def main():
    csv_path = configuration_variables['csv']['path']

    create_folder(configuration_variables['json']['path']['folder'])
    data = extract.open_csv_file_to_get_data(csv_path)
    file_number = configuration_variables['files']['first_file']
    if check_maximum_rows(data):
        json_path = f"{configuration_variables['json']['path']['file']}_{file_number}"
        load.write_to_json(json_path, data, configuration_variables['rows']['first'],
                           configuration_variables['rows']['max'])
    else:
        for index in range(configuration_variables['rows']['first'], count_data_rows(data),
                           configuration_variables['rows']['max']):
            json_path = f"{configuration_variables['json']['path']['file']}_{file_number}"
            load.write_to_json(json_path, data, index, index + configuration_variables['rows']['max'])
            file_number += configuration_variables['files']['next_file']


if __name__ == '__main__':
    main()
