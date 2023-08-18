from Json_assisstance.read_json_file import read_data
import json


def delete_project(pid: str, owner: str):
    new_data = list()

    try:
        old_data = read_data('Projects.json')
        for project in old_data:
            if pid == str(project['PID']):
                if project['Owner'] == owner:
                    print(f'Project with PID: {pid} was successfully deleted')
                    continue
                else:
                    new_data.append(project)
                    print('Permission denied')
            else:
                new_data.append(project)
        if new_data == old_data:
            print("nothing was deleted ")
        with open('Projects.json', 'w') as file_object:
            data = json.dumps(new_data, indent=4)  # convert list of dicts to string
            file_object.write(data)  # write data to the file
    except Exception as e:
        print(e)


def remove_project(email: str):
    pid = ''
    while not pid.isdigit():
        pid = input("Enter invalid project ID (PID): ")
    delete_project(pid, email)
