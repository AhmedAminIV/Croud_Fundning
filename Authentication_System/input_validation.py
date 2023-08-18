import re
from Json_assisstance.read_json_file import read_data


def name(name: str):
    try:
        if name.isalpha() and len(name) > 1:
            return True
        else:
            return False
    except Exception as e:
        return False


def email(email: str):
    email_regex = r'\b[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.[A-Za-z]{2,4}\b'
    try:
        email_flag = bool(re.match(email_regex, email))
        return email_flag
    except:
        return False


def unique_email(file: str, email):
    data_list = read_data(file)
    for dic in data_list:
        if dic["E-mail"] == email:
            print("Email is already used")
            return False
    return True


def password(pw: str):
    password_regex = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
    try:
        password_flag = bool(re.match(password_regex, pw))
        return password_flag
    except:
        return False


def password_match(pw1: str, pw2: str):
    if pw1 == pw2:
        return True
    else:
        return False


def phone(phone: str):
    phone_regex = r'^01[0125]{1}[0-9]{8}$'
    try:
        phone_flag = bool(re.match(phone_regex, phone))
        return phone_flag
    except:
        return False


def title_v(title: str):
    title_regex = r'^[A-Za-z\s]{1,50}[0-9]{0,10}$'
    try:
        title_flag = bool(re.match(title_regex, title))
        return title_flag
    except:
        return False


def details_v(details: str):
    details_regex = r'[A-Za-z\s0-9!@#$%&*()_-]{0,5000}'
    try:
        details_flag = bool(re.match(details_regex, details))
        return details_flag
    except:
        return False


def target_v(total_target: str):
    target_regex = r'^[1-9][0-9]{0,100}[\s]{1,2}[A-Z]{3}$'
    try:
        target_flag = bool(re.match(target_regex, total_target))
        return target_flag
    except:
        return False


def date(date: str):
    date_regex = r'^[0-9]{4}-((0[1-9])|(1[0-2]))-((0[1-9])|([1-2][0-9])|(3[0-1]))(\s((2[0-3])|([0-1][0-9])):[0-5][0-9]:[0-5][0-9]){0,1}$'
    try:
        date_flag = bool(re.match(date_regex, date))
        return date_flag
    except:
        return False


def end_date(start_date: str, end_date: str):
    try:
        if start_date > end_date:
            return False
        return True
    except:
        return False
