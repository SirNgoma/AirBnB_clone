#!/usr/bin/python3
""" Base Model class """

import uuid
from datetime import datetime

class BaseModel:
    """
    Base model class for all classes.
    """

    def __init__(self, *args,**kwargs):
        """initialize of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key,value)
            self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
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
