import unittest
from unittest.mock import patch
from main import main_func_call


class TestUserAuthentication(unittest.TestCase):

    @patch('main.authenticate_user')
    @patch('builtins.input', side_effect=['2', 'existing_user', 'existing_password'])
    def test_authenticate_user(self, mock_input, mock_authenticate_user):
        # Call the function that handles user input
        main_func_call()

        # Check if the authenticate_user function was called with the correct arguments
        mock_authenticate_user.assert_called_once_with('existing_user', 'existing_password')


if __name__ == '__main__':
    unittest.main()
