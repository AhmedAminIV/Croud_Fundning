from getpass import getpass
from Authentication_System.input_validation import *
from Json_assisstance.write_file import write_data


def registration():
    f_name_flag = False
    l_name_flag = False
    email_flag = False
    pw_flag = False
    pwc_flag = False
    ph_flag = False

    f_name = ''
    l_name = ''
    email_address = ''
    pw = ''
    ph_num = ''

    while not f_name_flag:
        f_name = input("First Name: ")
        f_name_flag = name(f_name)
        if not f_name_flag:
            print("Hint: [A-Za-z] only")

    while not l_name_flag:
        l_name = input("Last Name: ")
        l_name_flag = name(l_name)
        if not l_name_flag:
            print("Hint: [A-Za-z] only")

    while not email_flag:
        email_address = input("Email: ")
        email_flag = email(email_address) and unique_email('../users.json', email_address)
        if not email_flag:
            print("Please enter a valid Email! \nExample: myemail@smth.smth")

    while not pw_flag:
        pw = getpass("Password: ")
        pw_flag = password(pw)
        if not pw_flag:
            print("Weak password")

    while not pwc_flag:
        pw_confirm = getpass("confirm Password: ")
        pwc_flag = password_match(pw, pw_confirm)
        if not pwc_flag:
            print("Password doesn't match")

    while not ph_flag:
        ph_num = input("Phone: ")
        ph_flag = phone(ph_num)
        if not f_name_flag:
            print("Invalid Phone Number")

    user_data = {"first name": f_name, "last name": l_name, "E-mail": email_address, "Password": pw, "Phone": ph_num}
    write_data('users.json', user_data)
