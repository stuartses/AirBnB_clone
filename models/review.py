#!/usr/bin/python3
"""
module: review
define Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class: Review
    create class attributes place_id, user_id, text
    """
    place_id = ""
    user_id = ""
    text = ""
