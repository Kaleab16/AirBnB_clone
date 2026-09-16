#!/usr/bin/python3
"""File storage module."""

import json


class FileStorage:
    """Serialize instances to a JSON file and deserialize JSON file to objects."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        obj_dict = {}

        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)

            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review

            classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }

            for key, value in obj_dict.items():
                class_name = value["__class__"]

                if class_name in classes:
                    FileStorage.__objects[key] = classes[class_name](**value)

        except FileNotFoundError:
            pass
