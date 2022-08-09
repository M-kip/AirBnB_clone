#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
import pycodestyle
from models.review import Review
from models import review
from models.base_model import BaseModel


class TestReviewDocs(unittest.TestCase):
    """
    Runs Doc string and pycodestyle checks

    This class checks for proper code documentation
    if the class/ module contains __doc__ strings

    Methods
    -------
    test_review_pep8(self)
        Run checks with pycodestyle
    test_review_module_doc_string(self)
        Checks for module doc string
    test_review_class_doc_string(self)
        Checks for class doc strings
    test_review_test_pep8(self)
        Tests this script for pep compliance
    """

    def test_review_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("models/review.py", show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_review_test_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("tests/test_models/test_review.py",
                                    show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_module_doc_string(self):
        """ Checks if the doc string is present"""

        self.assertIsNot(review.__doc__, None, "review.py needs documentation")
        self.assertTrue(len(review.__doc__) >= 1, "review.py need doc string")

    def test_class_doc_string(self):
        """ Tests if the class doc string exists"""

        self.assertIsNot(Review.__doc__, None, "Review class needs doc str")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs doc str")


class TestReview(unittest.TestCase):

    """
    Test Cases for the Review class.

    Methods
    -------
    test_review_instantiation(self)
        Tests if the class can be instantiated
    test_review_variables(self)
        test for variables correctness
    """

    def test_review_instantiation(self):
        """
        Tests instantiation of Review class.

        Raises
        ------
        NotInstanceError
            if not an instance of Review
        NotTrueError
            if the instance is not a subclass of BaseModel
        """

        my_review = Review()
        self.assertIsInstance(my_review, Review)
        self.assertTrue(issubclass(type(my_review), BaseModel))

    def test_review_attributes(self):
        """
        Tests the attributes of Review class.

        Raises
        ------
        NotTrueError
            if instance doesn't contain attribute
        NotEqualError
            if instance attributes value don't match with test value'
        """
        my_review = Review()
        attributes = my_review.to_dict()
        for k, v in attributes.items():
            self.assertTrue(hasattr(my_review, k))
            self.assertEqual(attributes[k], v)


if __name__ == "__main__":
    unittest.main()
