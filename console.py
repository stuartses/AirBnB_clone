#!/usr/bin/python3

'import modules'
import cmd
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


"""AirBnB Clone - Console
This module creates a command interpreter to AirBnb Clone
Uses the cmd module

Holberton School
Foundations - Higher-level programming - Python
By Iván Darío Lasso and Stuart Echeverry
"""


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
    Creates a command interpreter
    """

    # intro = 'Welcome to AirBnB Console.\nType \'help\' to see options.\n'
    prompt = '(hbnb) '

    def emptyline(self):
        # when type empty line
        pass

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program\n'
        print()
        return True

    def do_create(self, arg):
        'Creates a new instance of BaseModel, saves it (to the JSON file)\n'

        if (arg == ""):
            print("** class name missing **")
            return

        # call a class by str
        try:
            get_class = getattr(sys.modules[__name__], arg)
            new_inst = get_class()
            new_inst.save()
            print(new_inst.id)

        except AttributeError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        'Prints the string representation of an instance based\n'

        args_list = shlex.split(arg)
        args_len = len(args_list)

        if args_len == 0:
            print("** class name missing **")
            return

        # call a class by str
        try:
            get_class = getattr(sys.modules[__name__], args_list[0])

        except AttributeError:
            print("** class doesn't exist **")
            return

        if args_len < 2:
            print("** instance id missing **")
            return

        all_storage = storage.all()
        look_key = args_list[0] + "." + args_list[1]

        try:
            print(all_storage[look_key])

        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id\n'

        args_list = shlex.split(arg)
        args_len = len(args_list)

        if args_len == 0:
            print("** class name missing **")
            return

        # call a class by str
        try:
            get_class = getattr(sys.modules[__name__], args_list[0])

        except AttributeError:
            print("** class doesn't exist **")
            return

        if args_len < 2:
                print("** instance id missing **")
                return

        all_storage = storage.all()
        look_key = args_list[0] + "." + args_list[1]

        try:
            del(all_storage[look_key])
            storage.save()

        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        'Prints all string representation of all instances\n'

        str_list = []

        if arg == "":
            all_storage = storage.all()
            for key_storage in all_storage.keys():
                str_list.append(str(all_storage[key_storage]))
            print(str_list)

        else:
            try:
                get_class = getattr(sys.modules[__name__], arg)
                all_storage = storage.all()

                for item_storage in all_storage.items():
                    obj_item = item_storage[1]

                    if obj_item.__class__.__name__ == arg:
                        str_list.append(str(obj_item))

                print(str_list)

            except AttributeError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        'Updates an instance based on the class name and id by\n'

        args_list = shlex.split(arg)
        args_len = len(args_list)
        print("len: {}". format(args_len))

        if args_len == 0:
            print("** class name missing **")
            return

        # call a class by str
        try:
            get_class = getattr(sys.modules[__name__], args_list[0])

        except AttributeError:
            print("** class doesn't exist **")
            return

        if args_len < 2:
            print("** instance id missing **")
            return

        all_storage = storage.all()
        look_key = args_list[0] + "." + args_list[1]

        try:
            obj_storage = all_storage[look_key]

        except KeyError:
                print("** no instance found **")
                return

        if args_len < 3:
            print("** attribute name missing **")
            return

        if args_len < 4:
            print("** value missing **")
            return

        actual_value = getattr(obj_storage, args_list[2])

        # cast value to attribute type
        new_value = type(actual_value)(args_list[3])

        setattr(obj_storage, args_list[2], new_value)
        print(obj_storage)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
