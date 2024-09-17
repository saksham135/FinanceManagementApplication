import unittest
from unittest.mock import patch, MagicMock
from addtransactions import transaction_options, insert_transaction, add_expense, update_transaction, delete_transaction


class TestTransactionOptions(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '1',  # Choice to add a new transaction
        '1', 'income', 'Salary', '5000', 'Monthly salary', '2023-08-01',  # Inputs for new transaction
        'no'  # Terminal choice
    ])
    @patch('addtransactions.insert_transaction')
    def test_add_transaction(self, mock_insert_transaction, mock_input):
        transaction_options()
        mock_insert_transaction.assert_called_once_with(
            1, 'income', 'Salary', 5000, 'Monthly salary', '2023-08-01'
        )

    @patch('builtins.input', side_effect=[
        '2',  # Choice to add expense
        '1', 'Food', '100', 'Grocery shopping', '2023-09-01',  # Inputs for expense
        'no'  # Terminal choice
    ])
    @patch('addtransactions.add_expense')
    def test_add_expense(self, mock_add_expense, mock_input):
        transaction_options()
        mock_add_expense.assert_called_once_with(
            1, 'Food', 100, 'Grocery shopping', '2023-09-01'
        )

    @patch('builtins.input', side_effect=[
        '3',  # Choice to update transaction
        '1', 'Salary', '5500', 'Updated salary', '2023-09-01',  # Inputs for updating transaction
        'no'  # Terminal choice
    ])
    @patch('addtransactions.update_transaction')
    def test_update_transaction(self, mock_update_transaction, mock_input):
        transaction_options()
        mock_update_transaction.assert_called_once_with(
            1, 'Salary', 5500, 'Updated salary', '2023-09-01'
        )

    @patch('builtins.input', side_effect=[
        '4',  # Choice to delete transaction
        '1', 'Salary',  # Inputs for deleting transaction
        'no'  # Terminal choice
    ])
    @patch('addtransactions.delete_transaction')
    def test_delete_transaction(self, mock_delete_transaction, mock_input):
        transaction_options()
        mock_delete_transaction.assert_called_once_with(
            1, 'Salary'
        )


if __name__ == '__main__':
    unittest.main()
