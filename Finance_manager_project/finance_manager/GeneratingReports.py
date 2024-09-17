#
from connect_db import *

def generating_reports():
    print('###########################################################')
    print('---------------------Reports Menu----------------------')
    print('#Choice1: For Printing Monthly Reports press 1')
    print('#Choice2: For Printing Yearly Reports press 2')
    rep_choice = (int(input('Please Enter Your Choice')))
    if rep_choice ==1:
        print('Example Format is "generate_monthly_report(1, 8, 2023)" ')
        re_uid = (int(input('Please Enter Your User Id')))
        re_mo = (int(input('Please Enter the Month Number to get its Reports')))
        year = (int(input('Please Enter the Year Number')))
        month_rep=generate_monthly_report(re_uid,re_mo,year)
        print(month_rep)
    if rep_choice ==2:
        print('Example Format is "generate_monthly_report(1,2023)" ')
        reyeuid = (int(input('Please Enter Your User Id')))
        reyear = (int(input('Please Enter the Year Number')))
        year_rep=generate_yearly_report(reyeuid,reyear)
        print(year_rep)
    terminal_choice()



import os


def terminal_choice():
    print('###########################################################')
    print('--------------------- Choice Menu ----------------------')
    print('Do you want to Clear the terminal and perform another Operations?')
    print('Please Write yes/no?')
    choice_terminal = (input('Enter Your Choice'))
    if choice_terminal == 'yes':
        clear_terminal()
        generating_reports()

    else:
        print("Thank you for using the transaction menu. Goodbye!")


def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')



# def generate_monthly_report(user_id, month, year):
#     connection = get_db_connection()
#     cursor = connection.cursor()
#
#     cursor.execute(
#         "SELECT category, type, SUM(amount) FROM transactions "
#         "WHERE user_id = %s AND MONTH(date) = %s AND YEAR(date) = %s GROUP BY category, type",
#         (user_id, month, year)
#     )
#     report = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return report

def generate_monthly_report(user_id, month, year):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Query to fetch the sum of amounts grouped by category and type
    cursor.execute(
        """
        SELECT 
            category, 
            type, 
            SUM(amount) AS total_amount 
        FROM transactions 
        WHERE user_id = %s AND MONTH(date) = %s AND YEAR(date) = %s 
        GROUP BY category, type
        """,
        (user_id, month, year)
    )

    report = cursor.fetchall()
    cursor.close()
    connection.close()
    return report


def generate_yearly_report(user_id, year):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Query to fetch the sum of amounts grouped by category and type for the whole year
    cursor.execute(
        """
        SELECT 
            category, 
            type, 
            SUM(amount) AS total_amount 
        FROM transactions 
        WHERE user_id = %s AND YEAR(date) = %s 
        GROUP BY category, type
        """,
        (user_id, year)
    )

    report = cursor.fetchall()
    cursor.close()
    connection.close()

    return report

