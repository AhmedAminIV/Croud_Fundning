from Json_assisstance.search_data import read_data
from Authentication_System.input_validation import date
from tabulate import tabulate

matched_dates = []


def search_by_date():
    search_flag = False
    search_key = ''
    while not search_flag:
        search_key = input("date: ")
        search_flag = date(search_key)
        if not search_flag:
            print("Invalid format\nFormat: YYYY-MM-DD[ HH:MM:SS]")
    data = read_data('Projects.json')
    for project in data:
        if project["Start_Time"] == search_key or project["End_Time"] == search_key:
            matched_dates.append(project)

    if len(matched_dates):
        header = matched_dates[0].keys()
        rows = [project.values() for project in matched_dates]
        print(tabulate(rows, header))
    else:
        print(f"0 Results were found for: {search_key}")