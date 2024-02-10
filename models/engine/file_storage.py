#!/usr/bin/python3
"""model that contains FileStorage class
"""
import json


class FileStorage:
    """class that contains to hidden attribute
    file pasth and object
    methods
    all, new, save, reload
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """create objects
        """
        return self.__objects

    def new(self, obj):
        """object key to value
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save to file
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """reload from file
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)

            from models.base_model import BaseModel
            from models.user import User
            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                model_class = eval(class_name)
                obj = model_class(**value)
                self.new(obj)
        except:
            pass
