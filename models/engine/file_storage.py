#!/usr/bin/python3
"""
"""
import json


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return self.__objects

    def new(self, obj):
        """
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)

            from models.base_model import BaseModel
            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                model_class = eval(class_name)
                obj = model_class(**value)
                self.new(obj)
