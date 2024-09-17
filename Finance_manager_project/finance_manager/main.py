
from registeruser import *
from Authenticate import *
from connect_db import *
import bcrypt


def main_func_call():
    print('###########################################################')
    print('Welcome to the Main Menu')
    print('###### Please Select One of the Choices ######')
    print('--------------- Choices -------------------')
    print('I. Choice 1: Register New User in the Database')
    print('II. Choice 2: Authenticate/Login the given user')
    print('--------------------------------------------')
    print('Please Enter Your choice according to the Given Numbers')

    choice = int(input('Enter Choice Number in Numeric Format only: '))

    if choice == 1:
        username = input('Please Enter New Username: ')
        password = input('Please Enter New Password: ')
        return register_user(username, password)

    elif choice == 2:
        print('-----------------------------------------------------')
        print(f'You selected Choice {choice}')
        print('Please Enter your Login Credentials')
        old_username = input('Please Enter your existing Username: ')
        old_password = input('Please Enter your existing Password: ')
        return authenticate_user(old_username, old_password)
    else:
        print('# ERROR: INVALID CHOICE')
        print('Please Enter the choice in the given format only')







# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_func_call()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
