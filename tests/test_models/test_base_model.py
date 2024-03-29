#!/usr/bin/python3
""" Unittests for BaseModel """

import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import datetime
import os


class BaseModelTests(unittest.TestCase):
    """Test cases against the BaseModel class"""
    def setUp(self):
        """Set up a common instance for tests"""
        self.model_obj = BaseModel()

    def test_BaseModel_attributes(self):
        """ Test on the class instance """

        self.model_obj.name = "My first model"
        self.model_obj.my_number = 90
        self.model_obj.save()
        model_json = self.model_obj.to_dict()

        self.assertEqual(self.model_obj.name, model_json['name'])
        self.assertEqual(self.model_obj.my_number, model_json['my_number'])
        self.assertEqual('BaseModel', model_json['__class__'])
        self.assertEqual(self.model_obj.id, model_json['id'])

    def test_save_method_creates_id(self):
        """ Test if the save method creates an id """
        self.model_obj.save()
        self.assertIsInstance(self.model_obj.id, str)

    def test_save_method_updates_timestamps(self):
        """ Test if the save method updates timestamps """
        self.model_obj.save()
        self.assertIsInstance(self.model_obj.created_at, datetime.datetime)
        self.assertIsInstance(self.model_obj.updated_at, datetime.datetime)

    def test_save(self):
        """testing the save class method """
        before_time = self.model_obj.updated_at
        self.model_obj.my_number = 33
        self.model_obj.save()
        new_time = self.model_obj.updated_at
        self.assertNotEqual(before_time, new_time)

    def test_to_dict(self):
        """ test cases for to_dict method """
        returned_dict = self.model_obj.to_dict()
        expcted_dict = self.model_obj.__dict__.copy()
        expcted_dict["__class__"] = self.model_obj.__class__.__name__
        expcted_dict["updated_at"] = self.model_obj.updated_at.isoformat()
        expcted_dict["created_at"] = self.model_obj.created_at.isoformat()
        self.assertDictEqual(expcted_dict, returned_dict)


if __name__ == '__main__':
    unittest.main(i)
