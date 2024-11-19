import os
import yaml

from Extract import extract
import Load.load as load

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def create_folder(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully")
    else:
        print(f"Directory '{dir_name}' already exists")


def main():
    create_folder(configuration_variables['json']['path']['folder'])

    data = extract.open_csv_file_to_get_data(configuration_variables['csv']['path'])
    load.create_report_files(data)


if __name__ == '__main__':
    main()
