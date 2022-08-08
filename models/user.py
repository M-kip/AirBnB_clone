#!/usr/bin/python3
"""
This module implements the user class
"""

from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """
        User class inherits from BaseModel class

        Attributes
        ----------
        email: str
            Email of the user
        password: str
            user password
        first_name: str
            first name of the user
        last_name: str
            last name of the user

        Methods
        -------
        to_dict(self)
            Overrides Base Class to_dict
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize instance and class variables"""

        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Overrides the base class to_dict method and
        adds User class atrributes
        """

        dictionary = super().to_dict()
        dictionary["email"] = self.__class__.email
        dictionary["password"] = self.__class__.password
        dictionary["first_name"] = self.__class__.first_name
        dictionary["last_name"] = self.__class__.last_name

        return dictionary
