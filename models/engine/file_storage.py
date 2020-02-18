#!/usr/bin/python3
"""
module: file_storage
serializa and deserealiza json files
"""

import json


class FileStorage():
    """
    class: FileStorage
    Serializa instance objects to a json file and deseraliza
    json file to a instance objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"
        Function: all
        return all objects stored in __objects dict
        """

        return self.__objects

    def new(self, obj):
        """
        Function: new
        create new key in the __object
        dict(<class name>.uuid-->instance object)
        """

        new_classname = obj.__class__.__name__
        new_id = obj.id
        new_key = "{}.{}".format(new_classname, new_id)
        self.__objects[new_key] = obj

    def save(self):
        """
        Function: save
        serializa objects in __object dict to a json file
        """
        # creates dictionary
        # __object key:-->to_dict of BaseModel
        obj_dic = {}
        for i in self.__objects.items():
            obj_dic[i[0]] = i[1].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(obj_dic))

    def reload(self):
        """
        Function: reload
        deseriaiza json file to a objects in __object dict
        only if file exist
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
