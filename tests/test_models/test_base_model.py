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


if __name__ == '__main__':
    unittest.main(i)
