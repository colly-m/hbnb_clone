#!/usr/bin/python3
"""Module to define a class FileStorage"""
import json
import models
import os


class FileStorage:
    """Defines a class FileStorage"""
    __file__path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objests in dictionary also accessing all stored objects"""
        return (self.__objects)

    def new(self, obj):
        """Adds an object into a dictionary with <obj class name>.id key"""
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects dictionary to JSON format and saves to specified
        __file_path
        """
        data = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fd:
            json.dump(data, fd)

    def reload(self):
        """"Method to deserialise JSON file"""
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as fd:
                FileStorage.__objects = json.load(fd)
            for key, obj in FileStorage.__objects.items():
                class_name = obj["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**obj)
        except FileNotFoundError:
            pass
