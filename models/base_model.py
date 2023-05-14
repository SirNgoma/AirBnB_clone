#!/usr/bin/python3
""" Base Model class """

import uuid
from datetime import datetime

class BaseModel:
    """
    Base model class for all classes.
    """
    id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    def __init__(self, **kwargs):
        """initialize of the class"""
        super().__init__(**kwargs)
        self.id = str9uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str to repres class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict_-}"

    def save(self):
        """updates or saves datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """TReturns a dict containing all keys, values of __dict__"""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["craeted_at"] dict_["created_at"].isoformat()
        dict_["updated_at"] = dict_["updated_at"].isofrmat()
        return dict_
