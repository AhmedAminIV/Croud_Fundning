from getpass import getpass
from Json_assisstance.search_data import search
from Projects.project_creation import create
from Projects.view_project import view
from Projects.edit_project import modify_project
from Projects.delete_project import remove_project
from Projects.search_project import search_by_date


def login():
    attempts = 0

    while attempts < 5:
        email = input("Email: ")
        pw = getpass("Password: ")

        if search('users.json', email, pw):
            print('Successfully logged in')
            logged_in(email)
        else:
            attempts += 1
            print(f"Invalid Email or Password\nAttempts left {5-attempts}")
    print('Exiting...')
    exit()


def logged_in(email: str):
    reply = '0'
    while reply != '1' or reply != '2' or reply != '3' or reply != '4' or reply != '5':
        reply = input("\n1) Create new project\n2) View projects \n3) Edit project\n4) Delete project\n5) Search "
                      "project by date\n6) Log out\n0) Exit\n\nChoice: ")
        if reply == '1':
            create(email)
        elif reply == '2':
            view()
        elif reply == '3':
            modify_project(email)
        elif reply == '4':
            remove_project(email)
        elif reply == '5':
            search_by_date()
        elif reply == '6':
            login()
        elif reply == '0':
            exit()
        else:
            print("Invalid input")
