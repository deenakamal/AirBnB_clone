#!/usr/bin/python3
""" Definition of City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init the Amenity object"""
        super().__init__(*args, **kwargs)
