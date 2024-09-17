from connect_db import *


def transaction_options():
    print('###########################################################')
    print('--------------------- Transaction Menu ----------------------')
    print('# Choice 1: For adding a new transaction in the database, press 1')
    print('# Choice 2: For adding a Expenses in the database, press 2')
    print('# Choice 3: For updating an existing transaction in the database, press 3')
    print('# Choice 4: For deleting an existing transaction in the database, press 4')

    trans_choice = int(input('Please Enter your choice: '))

    if trans_choice == 1:
        print('###########################################################')
        print('---------------- Adding New Transaction ----------------')
        print('Format for adding a new transaction should be like this:')
        print(1, 'income', 'August Salary', 5000, 'Monthly salary', '2023-08-01')

        uid = int(input('Please Enter user_id: '))
        t_type = input('Please Enter Transaction Type: ')
        print('Please Enter Trnsaction Type as income only to avoid errors in Database.')
        cat = input('Please Enter Category: ')
        amo = int(input('Please Enter the amount: '))
        desc = input('Please Enter the Description: ')
        date = input('Please Enter the Date in Format (YYYY-MM-DD): ')

        insert_transaction(uid, t_type, cat, amo, desc, date)

    elif trans_choice == 2:
        print('###########################################################')
        print('---------------- Adding Expenses ---------------')
        print('Example for updating an existing transaction can be like this:')
        print("1, expense, 50.75, Grocery Shopping, 2023-08-01")

        ep_uid = int(input('Please Enter your existing user_id: '))
        ep_category = input('Please Enter Expenses category: ')
        print('Please Enter Transaction Type as expense only to avoid errors in Database.')
        ep_amo = int(input('Please Enter the Expenses amount: '))
        ep_desc = input('Please Enter the Expense description: ')
        ep_date = input('Please Enter the Date in Format (YYYY-MM-DD): ')

        add_expense(ep_uid, ep_category, ep_amo, ep_desc, ep_date)

    elif trans_choice == 3:
        print('###########################################################')
        print('---------------- Updating Current Transaction ---------------')
        print('Example for updating an existing transaction can be like this:')
        print(1, 'Salary', 5500, 'Updated salary')

        up_uid = int(input('Please Enter your existing user_id: '))
        up_category = input('Please Enter your previous existing transaction category to update: ')
        up_amo = int(input('Please Enter the updated amount: '))
        up_desc = input('Please Enter the updated transaction description: ')
        up_date = input('Please Enter the Date in Format (YYYY-MM-DD): ')

        update_transaction(up_uid, up_category, up_amo, up_desc, up_date)

    elif trans_choice == 4:
        print('###########################################################')
        print('---------------- Deleting Existing Transaction ---------------')
        print('Example for deleting an existing transaction is:')

        del_uid = int(input('Please Enter your existing user_id: '))
        del_cat = input('Please Enter the existing category: ')

        delete_transaction(del_uid, del_cat)

    terminal_choice()


def add_expense(user_id, category, amount, description, date):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO transactions (user_id, type, category, amount, description, date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (user_id, 'expense', category, amount, description, date)
        )
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()
        print("Expense added successfully.")


def insert_transaction(user_id, transaction_type, category, amount, description, date):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = (
        "INSERT INTO transactions (user_id, type, category, amount, description, date) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )

    cursor.execute(query, (user_id, transaction_type, category, amount, description, date))

    connection.commit()
    cursor.close()
    connection.close()

    print("Transaction inserted successfully.")


def update_transaction(user_id, category, amount, description, date):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = (
        "UPDATE transactions SET amount = %s, description = %s, date = %s "
        "WHERE user_id = %s AND category = %s"
    )

    cursor.execute(query, (amount, description, date, user_id, category))

    connection.commit()
    cursor.close()
    connection.close()

    print("Transaction updated successfully.")


def delete_transaction(user_id, category):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = ("DELETE FROM transactions WHERE user_id = %s AND category = %s")
    cursor.execute(query, (user_id, category))

    connection.commit()
    cursor.close()
    connection.close()

    print("Transaction deleted successfully.")


def terminal_choice():
    print('###########################################################')
    print('--------------------- Choice Menu ----------------------')
    print('Do you want to Clear the terminal and perform another operation?')
    print('Please Write yes/no?')
    choice_terminal = input('Enter Your Choice: ')

    if choice_terminal == 'yes':
        clear_terminal()
        transaction_options()
    else:
        print("Thank you for using the transaction menu. Goodbye!")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')




