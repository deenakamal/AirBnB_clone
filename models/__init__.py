#!/usr/bin/python3
"""
__init__ used for make components,
distributed across multiple subdirectories
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
