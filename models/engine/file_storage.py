#!usr/bin/python3
"""
    module related to the file storage
    serialization and deserialization
"""
import json
import models
from models.base_model import BaseModel


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
        for key_id, objs in self.__objects.items():
            dic_to_store[key_id] = objs.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(dic_to_store, f)

    def reload(self):
        '''
            deserializes the JSON file stored in file.json
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                objects_to_load = json.load(f)
                for k, v in objects_to_load.items():
                    reloaded_obj = eval('{}(**v)'.format(v['__class__']))
                    self.__objects[k] = reloaded_obj

        except IOError:
            pass
