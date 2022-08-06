#!/usr/bin/python3
"""Defines a class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that defines properties of Amenity.

    Attributes:
        name (string): name of amenity.
    """
    name = ""
