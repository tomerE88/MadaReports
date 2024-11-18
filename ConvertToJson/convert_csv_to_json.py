import csv
import json


def open_csv_file(csv_path):
    with open(csv_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return csv_reader
