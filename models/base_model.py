#!/usr/bin/python3
"""
BaseModel that defines all other modules
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseModel class definition
    """
    def __init__(self, *args, **kwargs):
        """
        Instance constructor
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key in ["updated_at", "created_at"]:
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict returns a dictionary containing all keys/values
        """
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["updated_at"] = self.updated_at.isoformat()
        _dict["created_at"] = self.created_at.isoformat()
        return _dict

    def __str__(self):
        """
        String Representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        Updates the public instance attribute
        """
        self.updated_at = datetime.now()
        models.storage.save()
