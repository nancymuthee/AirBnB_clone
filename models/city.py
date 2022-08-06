#!/usr/bin/python3
"""Defines a class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines properties of City.

    Attributes:
        name (string): name of city.
        state_id (string): id of state.
    """
    state_id = ""
    name = ""
