#!/usr/bin/python3
""" Unittest cases """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import models
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ Test cases """

    def test_create(self):
        """ test """
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        model.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
