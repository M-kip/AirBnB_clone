#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
import pycodestyle
from models.state import State
from models import storage
from models import state


class TestStateDocs(unittest.TestCase):
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

    def test_state_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("models/state.py", show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_state_test_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("tests/test_models/test_state.py",
                                    show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_module_doc_string(self):
        """ Checks if the doc string is present"""

        self.assertIsNot(state.__doc__, None, "state.py needs documentation")
        self.assertTrue(len(state.__doc__) >= 1, "state.py need doc string")

    def test_class_doc_string(self):
        """ Tests if the class doc string exists"""

        self.assertIsNot(State.__doc__, None, "State class needs doc str")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs doc str")


class TestState(unittest.TestCase):

    """
    Test Cases for the State class.

    This class tests variables, behaviour
    and instantiation correctness

    Methods
    -------
    test_state_instantiation(self)
        test class instantiation
    test_state_attributes(self)
        tests the class variables
    """

    def test_state_instantiation(self):
        """
        Tests instantiation of State class.

        Raises
        -----
        assertIsInstanceError
            if the class create is not an instance of State
        """

        my_state = State()
        my_state.name = "illinois"
        my_state.save()
        self.assertIsInstance(my_state, State)

    def test_state_kwargs_instantiation(self):
        """
        Checks if the class can be instantiated using dic

        Raises
        ------
        NotInstanceError
            if the class is not of State
        """

        my_state = State()
        my_state.name = "illinois"
        attrs = my_state.to_dict()
        my_state2 = State(**attrs)
        self.assertIsInstance(my_state2, State)

    def test_state_attributes(self):
        """
        Tests the attributes of State class.

        Raises
        ------
        assertEqualError
            If variables values are not equal
        asserTrueError
            raises this error if class has no attribute
        """

        my_state = State()
        my_state.name = "illinois"
        attrs = my_state.to_dict()
        for k, v in attrs.items():
            self.assertTrue(hasattr(my_state, k))


if __name__ == "__main__":
    unittest.main()
