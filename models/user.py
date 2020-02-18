#!/usr/bin/python3
"""
module: user
define User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class: User
    create class attributes email, password
    firts_name and last_name in a User Class
    """
    email = ""
    password = ""
    firts_name = ""
    last_name = ""
