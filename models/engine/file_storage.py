#!/usr/bin/python3
"""File storage module."""

import json


class FileStorage:
    """Serialize instances to a JSON file and deserialize JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        objects_dict = {}

        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(self.__file_path, "r") as file:
                objects_dict = json.load(file)

            for key, value in objects_dict.items():
                class_name = value["__class__"]

                if class_name == "BaseModel":
                    from models.base_model import BaseModel
                    self.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass
