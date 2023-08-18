from Json_assisstance.read_json_file import read_data
import json
from Authentication_System.input_validation import *


def edit(old_record: dict):
    title_flag = False
    details_flag = False
    target_flag = False
    start_time_flag = False
    end_time_flag = False

    pid = old_record['PID']
    owner = old_record['Owner']
    title = old_record['Project_title']
    details = old_record['Details']
    target = old_record['Target']
    start_time = old_record['Start_Time']
    end_time = old_record['End_Time']

    print('You can keep the old data of any field by leaving it empty :)')

    while not title_flag:
        edited_title = input("Title: ")
        if len(edited_title) == 0:
            break
        title_flag = title_v(edited_title)
        if not title_flag:
            print("Invalid title\nExample: Title 15")
        else:
            title = edited_title

    while not details_flag:
        edited_details = input("Details: ")
        if len(edited_details) == 0:
            break
        details_flag = details_v(edited_details)
        if not details_flag:
            print("Invalid details")
        else:
            details = edited_details

    while not target_flag:
        edited_target = input("Target: ")
        if len(edited_target) == 0:
            break
        target_flag = target_v(edited_target)
        if not target_flag:
            print("Invalid target\nExample: 1000 EGP")
        else:
            target = edited_target

    while not start_time_flag:
        edited_start_time = input("Start Time: ")
        if len(edited_start_time) == 0:
            break
        start_time_flag = date(edited_start_time)
        if not start_time_flag:
            print("Invalid format\nFormat: YYYY-MM-DD[ HH:MM:SS]")
        else:
            start_time = edited_start_time

    while not end_time_flag:
        edited_end_time = input("End Time: ")
        if len(edited_end_time) == 0:
            break
        end_time_flag = date(edited_end_time) and end_date(start_time, edited_end_time)
        if not end_time_flag:
            print("Invalid format\nFormat: YYYY-MM-DD[ HH:MM:SS]")
        else:
            end_time = edited_end_time

    project_data = {"PID": pid, "Owner": owner, "Project_title": title, "Details": details, "Target": target,
                    "Start_Time": start_time, "End_Time": end_time}

    return project_data


def edit_project(pid: str, owner: str):
    new_data = list()

    try:
        old_data = read_data('Projects.json')
        for project in old_data:
            if pid == str(project['PID']):
                if project['Owner'] == owner:
                    print(f"Editing Project {project['PID']}")
                    edited_project = edit(project)
                    new_data.append(edited_project)
                else:
                    new_data.append(project)
                    print('Permission denied')
            else:
                new_data.append(project)
        if new_data == old_data:
            print("nothing was modified !!")
        with open('Projects.json', 'w') as file_object:
            data = json.dumps(new_data, indent=4)  # convert list of dicts to string
            file_object.write(data)  # write data to the file
    except Exception as e:
        print(e)


def modify_project(email: str):
    pid = ''
    while not pid.isdigit():
        pid = input("Enter invalid project ID (PID): ")
    edit_project(pid, email)
