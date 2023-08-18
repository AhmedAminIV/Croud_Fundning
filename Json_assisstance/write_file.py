import json

from Json_assisstance.read_json_file import read_data


def write_data(file_name, data):
    try:
        old_data = read_data(file_name)
        with open(file_name, 'w') as file_object:
            old_data.append(data)
            data = json.dumps(old_data, indent=4)  # convert list of dicts to string
            file_object.write(data)  # write data to the file
    except Exception as e:
        print(e)
