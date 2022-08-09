#!/usr/bin/python3
"""
    This module provides the base class which will be inherited by
    future classes


    The module holds one class
      BaseModel:
"""
import sys
import datetime
import uuid
import models


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
        Returns dictionary containing all the
        keys/values of __dict__ of the instance

"""

    email = ""
    my_number = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Parameters
        ----------
        *args: list
            The current time ( when the object is created)
        **kwargs: dictionary
        """

        if kwargs:
            for key, value in kwargs.items():
                if (key == "name"):
                    self.__class__.name = value
                elif (key == "my_number"):
                    self.my_number = value
                elif (key == "created_at"):
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif (key == "updated_at"):
                    self.updated_at = datetime.datetime.fromisoformat(value)
                elif (key == "id"):
                    self.id = uuid.UUID(value)
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Parameters
        ----------
        self: instance
           The current instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Return a dictionary containing all instance variables & class name
        """
        dictionary = self.__dict__
        if dictionary:
            dictionary["__class__"] = self.__class__.__name__
            dictionary["id"] = str(dictionary["id"])
            if isinstance(dictionary["created_at"], datetime.datetime):
                cre = dictionary["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
                dictionary["created_at"] = cre
            if isinstance(dictionary["updated_at"], datetime.datetime):
                upd = dictionary["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
                dictionary["updated_at"] = upd

        return dictionary

    def save(self):
        """ Updates the updated_at variable with the current time
        """

        self.updated_at = datetime.datetime.now().isoformat()
        models.storage.save()
