#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
    BaseClass manage all program
"""


class BaseModel:
    """
        that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            initializes BaseModel class
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            returns a string representation of the class
        """
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
            updates 'uṕdated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance:
        """
        dic_rpr = self.__dict__.copy()
        dic_rpr['__class__'] = type(self).__name__
        dic_rpr['created_at'] = self.created_at.isoformat()
        dic_rpr['updated_at'] = self.updated_at.isoformat()
        return (dic_rpr)
