import json
import yaml

config_file = open('config.yml', 'r')
configuration_variables = yaml.safe_load(config_file)


def dump_data(data):
    return json.dump(json.dumps(data, indent=configuration_variables['json']['space_between_rows']))
