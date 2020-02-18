#!/usr/bin/python3
""" Module: base_model """
from datetime import datetime
import uuid

from models import storage


class BaseModel:
    """ Class: BaseModel"""
    def __init__(self, *args, **kwargs):
        """ Function: __init__
        """
        if kwargs:
            for i in kwargs.items():
                val = i[1]
                if i[0] == "created_at":
                    val = datetime.strptime(i[1], '%Y-%m-%dT%H:%M:%S.%f')
                if i[0] == "updated_at":
                    val = datetime.strptime(i[1], '%Y-%m-%dT%H:%M:%S.%f')
                if i[0] != "__class__":
                    setattr(self, i[0], val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Function: __str__
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, str(self.__dict__))

    def save(self):
        """ Function: save
            Descripcion:update updated_at instance atrib with current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Function: to_dict
            Descripcion: return dict of a instance object, add __class__ key
                         with the name of the class (BaseModel) and change to
                         a isoformat to created and updated attribs
        """
        dictionary = dict(**self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
