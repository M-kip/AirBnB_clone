#!/usr/bin/python3
"""
Test case for the base model
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Creates a test runner for the base model

    """

    def my_model_test(self):
        """ Run class tests"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model.name)
        print(my_model)
        my_model.save()
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my model:")

        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key,
                  type(my_model_json[key]), my_model_json[key]))


if __name__ == "__main__":
    unittest.main()
