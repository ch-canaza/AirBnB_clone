#!/usr/bin/python3
"""
    module related to the file storage
    serialization and deserialization
"""
import json
import models
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        serializes instances to a JSON file and
        deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary
        """
        return (self.__objects)

    def new(self, obj):
        """
            sets in __objects the obj
            with key <obj class name>.id
        """
        if obj:
            self.__objects["{}.{}".format(str(type(obj).__name__),
                                          obj.id)] = obj

    def save(self):
        """
             serializes __objects to the JSON file (path: __file_path)
        """
        dic_to_store = {}
        for key_id, objs in self.__objects.items():  # test
            dic_to_store[key_id] = objs.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(dic_to_store, f)

    def reload(self):
        '''
        deserializes the JSON file
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                newobjects = json.load(f)
                for k, v in newobjects.items():
                    reloadedobj = eval('{}(**v)'.format(v['__class__']))
                    self.__objects[k] = reloadedobj

        except IOError:
            pass
