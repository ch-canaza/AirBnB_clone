#!/usr/bin/python3
"""
class that inherits from BaseModel
"""


from models.base_model import BaseModel

class Review(BaseModel):
    """
    class comntaining Reviews
    """

    place_id = ""
    user_id = ""
    text = ""
