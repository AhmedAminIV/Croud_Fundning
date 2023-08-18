from Authentication_System.Login import login
from Authentication_System.registration import registration

ans = '0'
while ans != '1' or ans != '2':
    ans = input("1) Sign in\n2) Sign up\n3) Exit\n\nChoice: ")
    if ans == '1':
        login()
    elif ans == '2':
        registration()
    elif ans == '3':
        break
    else:
        print("Invalid input")
