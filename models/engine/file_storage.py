#!/usr/bin/python3

"""Module: file_storage
This module defines the FileStorage Class to AirBnB project.
Used to access and edit a JSON file

Args:
    obj (obj): input instance of object used to create a new in dictionary

Atributes:
    __file_path (str): path to the JSON file (ex: file.json)
    __objects (dict): store all objects by <class name>.id

"""


import json


class FileStorage():
    """Class FileStorage
    Serializes an instance objects to a json file and deseralizes
    json file to a instance objects.

    Args:
        obj (obj): input object used to create a new in a dictionary

    Atributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dict): store all objects by <class name>.id

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Show all objects stored in __objects dict

        Return:
            __objects: dictionary with all data

        """

        return self.__objects

    def new(self, obj):
        """Creates a new key in the __object
        dict(<class name>.uuid-->instance object)

        Args:
            obj: input object used to create a new element __objects
        """

        new_classname = obj.__class__.__name__
        new_id = obj.id
        new_key = "{}.{}".format(new_classname, new_id)
        self.__objects[new_key] = obj

    def save(self):
        """Save new date in a instance of a Class
        serializes objects in __object dict to a json file
        """

        # creates dictionary
        # __object key:-->to_dict of BaseModel
        obj_dic = {}
        for i in self.__objects.items():
            obj_dic[i[0]] = i[1].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(obj_dic))

    def reload(self):
        """Read JSON File
        deserializes a json file to a objects in __object dict
        only if file exist and based on Class Name
        """

        try:
            with open(self.__file_path, "r") as f:
                json_line = json.load(f)
            for i in json_line.items():
                Key = i[0]
                dicclass = i[1]
                classname = dicclass["__class__"]
                if classname == "BaseModel":
                    from models.base_model import BaseModel
                    obj = BaseModel(**dicclass)
                    self.__objects[Key] = obj
                if classname == "User":
                    from models.user import User
                    obj = User(**dicclass)
                    self.__objects[Key] = obj
                if classname == "State":
                    from models.state import State
                    obj = State(**dicclass)
                    self.__objects[Key] = obj
                if classname == "Amenity":
                    from models.amenity import Amenity
                    obj = Amenity(**dicclass)
                    self.__objects[Key] = obj
                if classname == "Review":
                    from models.review import Review
                    obj = Review(**dicclass)
                    self.__objects[Key] = obj
                if classname == "City":
                    from models.city import City
                    obj = City(**dicclass)
                    self.__objects[Key] = obj
                if classname == "Place":
                    from models.place import Place
                    obj = Place(**dicclass)
                    self.__objects[Key] = obj

        except IOError:
            pass
