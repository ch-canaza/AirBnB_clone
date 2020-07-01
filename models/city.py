#!/usr/bin/python3
"""
class that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    class containing cities
    """

    state_id = ""
    name = ""
