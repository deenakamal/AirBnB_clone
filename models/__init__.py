#!/usr/bin/python3
"""
__init__ used for make components,
distributed across multiple subdirectories
"""
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


storage = FileStorage()
storage.reload()
