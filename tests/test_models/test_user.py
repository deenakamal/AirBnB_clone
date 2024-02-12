#!/usr/bin/python3
"""Unittest for User"""

import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """unittest for user class"""

    def test_create_user(self):
        """ create instance """
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """test cases"""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_save_and_reload_user(self):
        """" create user """
        user = User()
        user.first_name = "Alice"
        user.last_name = "Johnson"
        user.email = "alice.j@example.com"
        user.password = "password123"
        before_user_up = user.updated_at
        user.email = "updated@example.com"
        after_user_up = user.updated_at
        self.assertEqual(before_user_up, after_user_up)


if __name__ == '__main__':
    unittest.main()
