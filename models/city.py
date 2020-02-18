#!/usr/bin/python3
"""
module: city
define City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class: City
    create class attributes state_id, name
    """
    state_id = ""
    name = ""
