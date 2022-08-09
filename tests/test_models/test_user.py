#!/usr/bin/python3
"""
Test module for user module

This module tests module pep compliance,
if the module/class/function has doc string

Classes
-------
TestUserDocs:
    Implements doc and pep compliance checks
TestUserInitialization:
    Tests variables and initialization
"""

import unittest
import pycodestyle
from models.base_model import BaseModel
from models.user import User
from models import user


class TestUserDocs(unittest.TestCase):
    """
    Runs Doc string and pycodestyle checks

    This class checks for proper code documentation
    if the class/ module contains __doc__ strings

    Methods
    -------
    test_user_pep8(self)
        Run checks with pycodestyle
    test_user_module_doc_string(self)
        Checks for module doc string
    test_user_class_doc_string(self)
        Checks for class doc strings
    test_user_test_pep8(self)
        Tests this script for pep compliance
    """

    def test_user_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("models/user.py", show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_user_test_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("tests/test_models/test_user.py",
                                    show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_module_doc_string(self):
        """ Checks if the doc string is present"""

        self.assertIsNot(user.__doc__, None, "user.py needs documentation")
        self.assertTrue(len(user.__doc__) >= 1, "user.py need doc string")

    def test_class_doc_string(self):
        """ Tests if the class doc string exists"""

        self.assertIsNot(User.__doc__, None, "User class needs doc str")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs doc str")


class TestUserInitialization(unittest.TestCase):
    """
    Tests the user class for initialization and variables issues

    This class Implements methods for checking dictionary initialization
    and the normal way the class also offers methods to check variable
    values and types

    Methods
    -------
    test_UserInitialization(self)
        Test if user can be initialized
    test_user_initialization_kwargs(self)
        Test if class can be created form kwargs
    test_user_attributes(self)
        Test the class attributes if working correctly
    """

    def test_UserInitialization(self):
        """
        Initialize User class
        """

        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()

        self.assertIsInstance(my_user, User)

    def test_user_initialization_kwargs(self):
        """
        Test if the class can be initialized from a dict
        """

        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.last_name = "Doe"
        my_user2.email = "airbnb@mail.com"
        my_user2.password = "root"
        my_user2.save()
        keywords = my_user2.to_dict()

        my_user3 = User(**keywords)
        self.assertEqual(my_user2.id, str(my_user3.id))

    def test_user_attributes(self):
        """
        Tests if the class attributes are present and workin
        """
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        attrs = my_user.to_dict()
        for key, value in attrs.items():
            self.assertTrue(hasattr(my_user, key))
            self.assertEqual(attrs[key], value)


if __name__ == "__main__":
    unittest.main()
