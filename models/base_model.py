#!/usr/bin/python3
"""
    This module contains the base class which will be inherited by 
    future classes 

    The module holds one class
      BaseModel:
"""
import sys
import datetime
import uuid

class BaseModel(object):
    """
    Class that implements all methods and attributes inherited

    Attributes
    ----------
    id : str
        Holds the uuid
    created_at: datetime
        time when instance was created
    updated_at: datetime
        assign the time when instance was created
    
    Methods
    -------
    __str__(self)
         Returns string representation of the class
    save(self)
        Updates the public instance attribute updated_at with current datetime
    to_dict(self)
        Returns dictionary containing all the keys/values of __dict__ of the instance

"""

    def __init__(self, *args, **kwargs):
        """
        Parameters
        ----------
        *args: list
            The current time ( when the object is created)
        **kwargs: dictionary
        """

        if kwargs is not None:
            for key value in kwargs.items():
                if key == name:
                    self.name = value
                else if key == my_number:
                    self.my_number = value
                else if key == created_at:
                    self.created_at = datetime.datetime(value)
                else if key == updated_at:
                    self.updated_at = datetime.datetime(value)
                else if key == id:
                    self.id = value
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.datetime.now().strftime("%")
            self.updated_at = datetime.datetime.now().strftime("%")
            self.name = None
            self.my_number = None


    def __str__(self):
        """
        Parameters
        ----------
        self: instance
           The current instance
        """
        return f"(<{self.__class__}> ({self.id}) <{self.__dict__}>)"

    def to_dict(self):
        """
        Return a dictionary containing all instance variables plus the class name
        """
        dictionary = self.__dict__()
        dictionary["__class__"] = self.__class__
        dictionary["created_at"] = dictionary["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictionary["updated_at"] = dictionary["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")

        return dictionary

    def save(self):
        """ Updates the updated_at variable with the current time """

        self.updated_at = datetime.datetime.now()

