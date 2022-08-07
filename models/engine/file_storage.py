#!/usr/bin/python3
"""
    This module implements the storage engine which
    it's main function is to serialize/deserialize objects
    to and from json format
"""
import json


class FileStorage:
    """
        Serialize and Deserialize objects

        Attributes
        ----------
        __file_path: str
            path to the JSON file
        __objects: dict
            empty dict to store objects

        Methods
        -------
        all(self)
            returns dictionary __object
        new(self)
            set in __object the obj with key <obj class name>.id
        save(self)
            Serializes __objects to JSON file
        reload(self)
            deserializes the JSON file to __objects
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """ returns the dictionary """

        return FileStorage.__objects

    def new(self, obj):
        """ Sets obj in __objects with the key <obj class name>.id """

        FileStorage.__objects[obj["id"]] = obj

    def save(self):
        """ Serializes obj to JSON  and save to file"""

        with open(FileStorage.__file_path, "w") as file_json:
            json.dump(FileStorage.__objects, file_json)

    def reload(self):
        """ Deserializes JSON file back to obj"""

        if FileStorage.__file_path:
            with open(FileStorage.__file_path, "r") as json_file:
                FileStorage.__objects = json.load(json_file)
