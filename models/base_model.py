#!/usr/bin/python3
"""a module that contains class BaseModel
"""
from datetime import datetime
import uuid
from models.__init__ import storage

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """class BaseModel that contains methods
    instatlize with uniq id
    string represtation
    dictionary represtation
    saves to a json file
    """
    def __init__(self,  *args, **kwargs):
        """inistantization with uniq id if no arguments
        else sets attribute with specific information
        """
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
            storage.save()

    def __str__(self):
        """string represtantion
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """saves to a storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """dictionary represtation of data
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        if 'created_at' in obj_dict:
            obj_dict['created_at'] = obj_dict['created_at'].strftime(time)
        if 'updated_at' in obj_dict:
            obj_dict['updated_at'] = obj_dict['updated_at'].strftime(time)
        return obj_dict
