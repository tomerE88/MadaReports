import os
import yaml

from Extract import extract
import Load.load as load

config_file = open('ConvertToJson/config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def create_folder(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully")
    else:
        print(f"Directory '{dir_name}' already exists")


def main():
    create_folder(configuration_variables['json']['path']['folder'])
    # csv_file = input("Enter csv file path: ")
    csv_file = configuration_variables['csv']['path']

    data = extract.open_csv_file_to_get_data(csv_file)
    load.create_report_files(data)


if __name__ == '__main__':
    main()
