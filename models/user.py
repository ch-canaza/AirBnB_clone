#!/usr/bin/python3

"""
user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class to create user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
