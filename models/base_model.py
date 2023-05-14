#!/usr/bin/python3
""" Base Model class """

import uuid
from datetime import datetime

class BaseModel:
    """
    Base model class for all classes.
    """

    def __init__(self):
        """initialize of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str to repres class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates or saves datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """TReturns a dict containing all keys, values of __dict__"""
        data = dict(self.__dict__)
        data["__class__"] = type(self).__name__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
