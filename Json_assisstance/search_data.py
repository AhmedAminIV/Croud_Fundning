from Json_assisstance.read_json_file import read_data


def search(file, email, pw):
    data = read_data(file)
    for user in data:
        if user['E-mail'] == email and user['Password'] == pw:
            return True
    else:
        return False
