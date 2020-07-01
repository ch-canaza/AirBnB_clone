#!/usr/bin/python3
"""
    file that initializes the file storage
"""


from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

all_classes = {"User": User, "BaseModel": BaseModel,
               "Place": Place, "State": State,
               "City": City, "Amenity": Amenity,
               "Review": Review}
storage = FileStorage()
storage.reload()
