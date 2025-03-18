import unittest

from rollee.account import Account
from rollee.solution import get_accounts_for_user


class TestSolution(unittest.TestCase):
    """Test the module rollee"""

    @classmethod
    def setUpClass(cls):
        """Extract accounts for valid user id"""
        cls.accounts = get_accounts_for_user(
            "engr.abidbaig@gmail.com",
            "Abid@rollee",
            "f1e13e83-fcd6-4990-b18b-022c6fc1ab80",
        )

    def test_total_accounts(self):
        """
        Should return 2 accounts for user id
        """
        self.assertEqual(len(self.accounts), 2)

    def test_accounts_details(self):
        """
        Should have these exact account details
        """
        self.assertEqual(
            self.accounts,
            [
                Account(
                    account_id="4a650c7b-2ee6-4625-95a8-53d7e736c0d6",
                    name="Taylor Lloyd",
                    email="TaylorLloyd@teleworm.us",
                    platform_name="Etsy",
                    country="MA",
                    currency="EUR",
                    gross_earnings=1459.94,
                ),
                Account(
                    account_id="c7cc3feb-64e4-4410-bcb9-33d88c1ffc55",
                    name="Anne Herrmann",
                    email="AnneHerrmann@teleworm.us",
                    platform_name="Creme de la Creme",
                    country="MA",
                    currency="EUR",
                    gross_earnings=381.37,
                ),
            ],
        )

    def test_invalid_credentials(self):
        """
        Should raise exception for invalid credentials with message 'Invalid credentials'
        """
        self.assertRaisesRegex(
            Exception,
            "Invalid credentials",
            get_accounts_for_user,
            "invalid_username",
            "whatever123",
            "f1e13e83-fcd6-4990-b18b-022c6fc1ab80",
        )

    def test_invalid_user_id(self):
        """
        Should raise exception if user id doesn't exist with message 'User not found'
        """
        self.assertRaisesRegex(
            Exception,
            "User not found",
            get_accounts_for_user,
            "engr.abidbaig@gmail.com",
            "Abid@rollee",
            "f1e13e83-fcd6-4990-b18b-022c6fc1ab81",
        )
