from Authentication_System.input_validation import *
from Json_assisstance.write_file import write_data


def create(user_email: str):
    title_flag = False
    details_flag = False
    target_flag = False
    start_time_flag = False
    end_time_flag = False

    title = ''
    details = ''
    target = ''
    start_time = ''
    end_time = ''

    data = read_data('Projects.json')
    PID = data[-1]['PID'] + 1

    while not title_flag:
        title = input("Title: ")
        title_flag = title_v(title)
        if not title_flag:
            print("Invalid title\nExample: Title 15")

    while not details_flag:
        details = input("Details: ")
        details_flag = details_v(details)
        if not details_flag:
            print("Invalid details")

    while not target_flag:
        target = input("Target: ")
        target_flag = target_v(target)
        if not target_flag:
            print("Invalid target\nExample: 1000 EGP")

    while not start_time_flag:
        start_time = input("Start Time: ")
        start_time_flag = date(start_time)
        if not start_time_flag:
            print("Invalid format\nFormat: YYYY-MM-DD[ HH:MM:SS]")

    while not end_time_flag:
        end_time = input("End Time: ")
        end_time_flag = date(end_time) and end_date(start_time, end_time)
        if not end_time_flag:
            print("Invalid format\nFormat: YYYY-MM-DD[ HH:MM:SS]")

    project_data = {"PID": PID, "Owner": user_email, "Project_title": title, "Details": details, "Target": target,
                    "Start_Time": start_time, "End_Time": end_time}
    write_data('Projects.json', project_data)
