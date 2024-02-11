#!/usr/bin/python3
""" Definition of Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
