from connect_db import *


def budget_menu():
    print('###########################################################')
    print('-------------------- Budget Menu ----------------------')
    print('# Choice 1: For Setting Budget press 1')
    print('# Choice 2: For Checking Budget press 2')

    bud_choice = int(input('Please Enter Your Choice: '))

    if bud_choice == 1:
        print('Example Format is "(1, income, 300)"')
        bud_uid = int(input('Please Enter Your User ID: '))
        bud_cat = input('Please Enter the Category (e.g., income): ')
        bud_limit = int(input('Please Enter Your Monthly Limit: '))
        set_budget(bud_uid, bud_cat, bud_limit)

    elif bud_choice == 2:
        print('Example Format is check_budget(1)')
        ch_uid = int(input('Please Enter Your User ID: '))
        check_budget(ch_uid)

    clear_terminal()


def set_budget(user_id, category, monthly_limit):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO budgets (user_id, category, monthly_limit) VALUES (%s, %s, %s)",
        (user_id, category, monthly_limit)
    )

    connection.commit()
    cursor.close()
    connection.close()

    print("Budget added successfully.")


def check_budget(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Retrieve total spending per category for the user
        cursor.execute(
            "SELECT category, SUM(amount) FROM transactions "
            "WHERE user_id = %s GROUP BY category",
            (user_id,)
        )
        spending = cursor.fetchall()

        # Retrieve budget limits for the user
        cursor.execute("SELECT category, monthly_limit FROM budgets WHERE user_id = %s", (user_id,))
        budgets = cursor.fetchall()

        # Notify if spending exceeds the budget for any category
        budget_exceeded = False
        for spend in spending:
            for budget in budgets:
                if spend[0] == budget[0] and spend[1] > budget[1]:
                    print(f"Alert: Budget exceeded in {spend[0]} category! "
                          f"Spent {spend[1]}, Budget {budget[1]}")
                    budget_exceeded = True

        if not budget_exceeded:
            print("You are within your budget limits.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()


import os


def terminal_choice():
    print('###########################################################')
    print('--------------------- Choice Menu ----------------------')
    print('Do you want to clear the terminal and perform another operation?')
    print('Please write yes/no:')

    choice_terminal = input('Enter Your Choice: ')

    if choice_terminal.lower() == 'yes':
        clear_terminal()
    else:
        print("Thank you for using the transaction menu. Goodbye!")


def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    budget_menu()
