#!/usr/bin/python3
"""
This module implements the user class
"""

from models.base_model import BaseModel


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
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize Super class and current class

        Parameters
        ----------
        args: list
            List of arguments
        kwargs: dict
            Dict of args
        """

        super().__init__(kwargs)
        storage.new(self.to_dict)

    def to_dict(self):
        """
        Overrides the base class to_dict method and
        adds User class atrributes
        """

        dictionary = super().to_dict()
        dictionary[User.email] = User.email
        dictionary[User.password] = User.password
        dictionary[User.first_name] = User.first_name
        dictionary[User.last_name] = User.last_name

        return dictionary
