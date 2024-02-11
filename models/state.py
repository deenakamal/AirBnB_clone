#!/usr/bin/python3
""" Definition of State Class """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class State """
    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
