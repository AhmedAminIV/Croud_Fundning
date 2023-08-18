from Json_assisstance.read_json_file import read_data
from tabulate import tabulate


def view():
    data = read_data('Projects.json')
    header = data[0].keys()
    rows = [project.values() for project in data]
    print(tabulate(rows, header))