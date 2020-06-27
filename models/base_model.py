#!/usr/bin/python3
import uuid
import models
from datetime import datetime


"""
    BaseClass
"""


class BaseModel:
    """
        that defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
            initializes BaseModel class
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
        """return (self.updated_at)"""

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance:
        """
        dic_rpr = self.__dict__.copy()
        dic_rpr['__class__'] = type(self).__name__
        dic_rpr['created_at'] = self.created_at.isoformat()
        dic_rpr['updated_at'] = self.updated_at.isoformat()
        return (dic_rpr)
