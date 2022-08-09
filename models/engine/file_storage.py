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

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary

        Parameters
        ----------
        cls: str optional
            class objects to return
        """

        if cls is not None:
            new_dict = {}
            for key, value in self.__class__.__objects:
                if cls == value.__class__.__name__:
                    new_dict[key] = value
                return new_dict
        return self.__class__.__objects

    def new(self, obj):
        """ Sets obj in __objects with the key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes obj to JSON  and save to file
        """

        json_objects = {}
        for key in self.__class__.objects.keys():
            json_objects[key] = self.__class__.__objects[key].to_dict()
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path, "w") as file_json:
                    json.dump(json_objects, file_json)
            except FileNotFoundError as err:
                pass

    def reload(self):
        """
        Deserializes JSON file back to obj
        """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        objs = {"Amenity": Amenity, "BaseModel": BaseModel,
                "City": City, "Place": Place, "Review": Review,
                "State": State, "User": User}
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path, "r") as json_file:
                    json_objs = json.load(json_file)
                    for key in json_objs.keys():
                        self.__class__.__objects[key] = \
                            objs[json_objs[key]["__class__"]](**json_objs[key])
            except FileNotFoundError as err:
                pass
