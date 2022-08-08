#!/usr/bin/python3
"""
Test case for the base model
"""

import unittest
import pycodestyle
from models.base_model import BaseModel
from models import base_model

class TestBaseModelDocs(unittest.TestCase):
    """
    Implements tests for the base class

    The test checks if the base_model file conforms to pep8
    and the correct documentation

    Methods
    -------
    test_base_model(self)
        Run pycodestyle tests
    """

    def test_base_model(self):
        """ checks if the base_model file conforms to pep8 style """
        style =pycodestyle.Checker("models/base_model.py", show_source = True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 error and Warnings")

    def test_base_model_test(self):
        """ Tests this file for PEP8 errors"""

        style = pycodestyle.Checker("tests/test_models/test_base_model.py", show_source = True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 errors & Warnings")

    def test_module_doc_string(self):
        """ Checks if the doc string is present"""

        self.assertIsNot(base_model.__doc__, None, "base_model.py needs documentation")
        self.assertTrue(len(base_model.__doc__) >= 1, "base_model.py need doc string")

    def test_class_doc_string(self):
        """ Tests if the class doc string exists"""

        self.assertIsNot(BaseModel.__doc__, None, "BaseModel class needs doc str")
        self.assertTrue(len(BaseModel.__doc__) >= 1, "BaseModel class needs doc str")

class TestBaseModel(unittest.TestCase):
    """
    This class tests the instances of the base class

    """
    def test_instance(self):
        """
        Tests if is an instance of the base class
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertIsInstance(my_model, BaseModel)

    def test_variables(self):
        """
        Tests the variables in BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_kwargs(self):
        """
        Test if the class can be initialized with a dict
        """

        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        temp_dict = my_model.to_dict()
        my_model2 = BaseModel(**temp_dict)
        self.assertIsInstance(my_model2, BaseModel)


if __name__ == "__main__":
    unittest.main()
