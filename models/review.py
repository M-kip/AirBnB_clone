#!/usr/bin/python3
"""Module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review."""
    place_id = ""
    user_id = ""
    text = ""

    def to_dict(self):
        """Overrides base class to_dict"""

        dictionary = super().to_dict()
        dictionary["place_id"] = self.__class__.place_id
        dictionary["user_id"] = self.__class__.user_id
        dictionary["text"] = self.__class__.text

        return dictionary
