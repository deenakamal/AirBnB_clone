#!/usr/bin/python3
""" Definition of Amenity Class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity """
    name = ""

        def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
