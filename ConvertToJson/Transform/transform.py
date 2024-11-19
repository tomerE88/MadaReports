import yaml

config_file = open('ConvertToJson/config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def convert_rows_to_dictionary(csv_reader):
    data = {}
    counter = configuration_variables['rows']['first_row']
    for row in csv_reader:
        key = counter
        counter += configuration_variables['rows']['next_row']
        data[key] = row

    return data
