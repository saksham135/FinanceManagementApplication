import unittest
from unittest.mock import patch
from main import main_func_call


class TestUserRegistration(unittest.TestCase):

    @patch('main.register_user')
    @patch('builtins.input', side_effect=['1', 'new_user', 'new_password'])
    def test_register_user(self, mock_input, mock_register_user):
        # Call the function that handles user input
        main_func_call()

        # Check if the register_user function was called with the correct arguments
        mock_register_user.assert_called_once_with('new_user', 'new_password')


if __name__ == '__main__':
    unittest.main()
