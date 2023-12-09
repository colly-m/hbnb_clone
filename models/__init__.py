#!/usr/bin/pyhon3
"""Module for __init__ model directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
