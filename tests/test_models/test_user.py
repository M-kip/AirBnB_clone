#!/usr/bin/python3
"""
Test module for user module

This module tests module pep compliance,
if the module/class/function has doc string

Classes
-------
TestUserDocs:
    Implements doc and pep compliance checks
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

        self.assertIsNot(User.__doc__, None, "BaseModel class needs doc str")
        self.assertTrue(len(User.__doc__) >= 1,
                        "BaseModel class needs doc str")


if __name__ == "__main__":
    unittest.main()
