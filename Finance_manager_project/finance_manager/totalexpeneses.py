from connect_db import *


def us_id():
    print('###########################################################')
    print('---------------- Calculate User Expenses and Savings ---------------')
    u_id = int(input('Please Enter the user ID to calculate all the user summaries, expenses, and savings: '))
    print_expense(u_id)


def cal_total_expense(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT 
            SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS total_income,
            SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_expenses
        FROM transactions
        WHERE user_id = %s
        """,
        (user_id,)
    )

    result = cursor.fetchone()

    total_income = result[0] if result[0] is not None else 0
    total_expenses = result[1] if result[1] is not None else 0
    total_savings = total_income - total_expenses

    cursor.close()
    connection.close()

    return {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'total_savings': total_savings
    }


def print_expense(user_id):
    summary = cal_total_expense(user_id)
    print(f"Financial Summary for User ID {user_id}:")
    print(f"Total Income: ${summary['total_income']:.2f}")
    print(f"Total Expenses: ${summary['total_expenses']:.2f}")
    print(f"Total Savings: ${summary['total_savings']:.2f}")

# # Example usage
# print_financial_summary(1)