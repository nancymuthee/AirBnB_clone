#!/usr/bin/python3
"""Defines a class Base"""
import uuid
from datetime import datetime


class BaseModel:
    """ Class that defines properties of base """

    def __init__(self):
        """ Creates new instances of Base """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns a string represation of class details.

        Returns:
            str: class details
        """
        string = "["
        string += str(self.__class__.__name__) + '] ('
        string += str(self.id) + ') ' + str(self.__dict__)
        return string

    def save(self):
        """Update public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance.

        Returns:
            dict: key/value pairs.
        """
        dict_ = self.__dict__.copy()
        dict_['__class__'] = self.__class__.__name__
        dict_['created_at'] = self.created_at.isoformat()
        dict_['updated_at'] = self.updated_at.isoformat()
        return dict_
