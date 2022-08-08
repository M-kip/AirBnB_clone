#!/usr/bin/python3
"""Module for Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a Place."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def to_dict(self):
        """Overrides base __dict__ to add class vars"""

        dictionary = super().to_dict()
        dictionary["city_id"] = self.__class__.city_id
        dictionary["user_id"] = self.__class__.user_id
        dictionary["name"] = self.__class__.name
        dictionary["description"] = self.__class__.description
        dictionary["number_rooms"] = self.__class__.number_rooms
        dictionary["number_bathrooms"] = self.__class__.number_bathrooms
        dictionary["max_guest"] = self.__class__.max_guest
        dictionary["price_by_night"] = self.__class__.price_by_night
        dictionary["latitude"] = self.__class__.latitude
        dictionary["longitude"] = self.__class__.longitude
        dictionary["amenity_ids"] = self.__class__.amenity_ids

        return dictionary
