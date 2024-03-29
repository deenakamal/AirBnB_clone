#!usr/bin/python3
""" File storage module """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    FileStorage class
    """
    CLASSES_DICT = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
            "State": State
            }

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """init"""
        pass

    def all(self):
        """Returns all objects in BaseModel class(in dictionary)"""
        return self.__objects

    def save(self):
        """"
        Serialize BaseModel objects in __objects to json objects
        """
        with open(self.__file_path, "w", encoding='utf-8') as file_:
            dic_ = {}
            for key, value in self.__objects.items():
                dic_[key] = value.to_dict()
            json.dump(dic_, file_)

    def new(self, obj):
        """adds new objects to __objects"""
        new_obj = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({new_obj: obj})

    def reload(self):
        """BaseModel class representing format."""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file_:
                json_objects = json.load(file_)
            for key, serialized_obj in json_objects.items():
                constractor = serialized_obj["__class__"]
                class_n = CLASSES_DICT(**serialized_obj)
                self.__objects[key] = class_n

        except Exception as e:
            pass
