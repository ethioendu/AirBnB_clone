#!/usr/bin/python3
"""module that contains class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that contains 3 attribute place_id(str)
    user_id(str)
    text(str)
    """
    place_id = ""
    user_id = ""
    text = ""
