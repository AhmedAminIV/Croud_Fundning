import json


def read_data(file_name):
    try:
        with open(file_name, 'r') as file_object:
            data = file_object.read()
            dict_data = json.loads(data)
            return dict_data
    except Exception as e:
        print(e)

