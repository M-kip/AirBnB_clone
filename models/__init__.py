#!/usr/bin/python3
""" Initializes the module"""
from models.engine import file_storage

storage = file_storage.FileStorage(path="json.json")
storage.reload()
