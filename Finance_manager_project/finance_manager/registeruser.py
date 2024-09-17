from connect_db import *
import bcrypt
import os
from Authenticate import *


def register_user(username, password):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Insert the new user into the database
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )
        connection.commit()
        print("User registered successfully.")
        terminal_choice()
    except mysql.connector.IntegrityError:
        print("Username already exists.")
    finally:
        cursor.close()
        connection.close()


def terminal_choice():
    print('###########################################################')
    print('--------------------- Choice Menu ----------------------')
    print('Do you want to Login?')
    print('Please Write yes/no?')
    choice_terminal = (input('Enter Your Choice'))
    if choice_terminal == 'yes':
        clear_terminal()
        print('Please Enter your Login Credentials')
        old_username = input('Please Enter your existing Username: ')
        old_password = input('Please Enter your existing Password: ')
        return authenticate_user(old_username, old_password)


    else:
        print("Thank you for using the transaction menu. Goodbye!")


def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')