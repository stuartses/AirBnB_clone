#!/usr/bin/python3

"""Module: base_model
This module defines the BaseModel Class to AirBnB project.

Atributes:
    id (str): assign with an uuid when an instance is created
    created_at (datetime): assign with the current datetime
                           when an instance is created
    updated_at (datetime): assign with the current datetime when
                           an instance is created and it will be
                           updated every time you change your object

"""


from datetime import datetime
import uuid

from models import storage


class BaseModel:
    """Class BaseModel
    BaseModel is the principal class to operate program
    Here the id and date are generated.

    Args:
        *args: list of data to create or modify an instance
        **kwargs: dictionary of data to create or modify an instance

    Atributes:
        id (str): assign with an uuid when an instance is created
        created_at (datetime): assign with the current datetime
                               when an instance is created
        updated_at (datetime): assign with the current datetime when
                               an instance is created and it will be
                               updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """Initializes a instance os BaseModel

        Args:
            *args: list of data to create or modify an instance
            **kwargs: dictionary of data to create or modify an instance
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
        """Replace the Method __str__
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, str(self.__dict__))

    def save(self):
        """Update instance with new current time
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dict of a instance object, add __class__ key
        with the name of the class (BaseModel) and change to
        a isoformat to created and updated attribs

        Return:
            dictionary: dictionary of a instance object

        """

        dictionary = dict(**self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
