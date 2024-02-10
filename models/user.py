#!/usr/bin/python3
"""model that contains one class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that defines public attributes
    """
    email = ""
    password = ""
    first_name =""
    last_name = ""
