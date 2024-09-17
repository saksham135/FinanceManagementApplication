from backup_user_data import *
from connect_db import *
from addtransactions import *
import bcrypt
from GeneratingReports import *
from totalexpeneses import *
from budgets import *
from restore_db import *



def authenticate_user(username, password):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the user's hashed password and user_id from the database
        cursor.execute("SELECT id, password_hash FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result:
            user_id, password_hash = result[0], result[1]

            # Check if the entered password matches the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
                print("Login successful! Now you can proceed with the application.")
                print(f"Your user ID is: {user_id}")
                print('--------------- Select Choices -----------------')
                print('# Choice 1: Transaction-Based Choices')
                print('# Choice 2: Generate Reports')
                print('# Choice 3: Calculate Total Income, Expenses, and Savings')
                print('# Choice 4: Setting and Checking Your Budget')
                print('# Choice 5: For Backup the DataBase.')
                print('# Choice 6: For Restoring the Database.')

                choice = int(input('Enter Choice: '))

                if choice == 1:
                    transaction_options()
                elif choice == 2:
                    generating_reports()
                elif choice == 3:
                    us_id()
                elif choice == 4:
                    budget_menu()
                elif choice==5:
                    create_backup()
                elif choice==6:
                    restore_backup()
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

    return False






