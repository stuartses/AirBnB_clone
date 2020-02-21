#!/usr/bin/python3

"""AirBnB Clone - Console
This module creates a command interpreter to AirBnb Clone
Uses the cmd module

Holberton School
Foundations - Higher-level programming - Python
By Iván Darío Lasso and Stuart Echeverry
"""

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


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand

    Creates a command interpreter by Air BnB Clone

    Args:
        arg (str): Human readable string that is used by console
                   to do some action.

    Attributes:
        prompt (str): Built-in attribute of Cmd Class that allows
                      to write a personal prompt text.
        intro (str): Built-in atribute of Cmd class that allows
                     to write a personal wellcome text.
    """

    # intro = 'Welcome to AirBnB Console.\nType \'help\' to see options.\n'
    prompt = '(hbnb) '

    def emptyline(self):
        """
        This function is executed when user type ENTER without any argument
        """

        pass

    def do_quit(self, arg):
        """
        Command to quit and exit the Console.

        Use: quit
        """

        return True

    def do_EOF(self, arg):
        """
        Command to quit and exit the Console by EOF (CTRL + D).
        """

        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of a ClassName and saves it (to the JSON file)
        and return the id of the new instance.

        Use: create <class name>
        Ex: create BaseModel

        Args:
            arg (str): Name of the class to create instance
                       (BaseModel, User, State, City, Amenity, Place, Review).

        """

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
        """
        Prints the string representation of an instance based in class
        and instance id.

        Use: show <class name> <id>
        Ex: show BaseModel b9132a3f-0ffd-49df-950d-7b257dcddbc7

           Args:
               arg (str): The name of the class and id, separated by space

        """

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
        """
        Deletes an instance based on the class name and id.
        And update JSON File.

        Use: destroy <class name> <id>
        Ex: destroy BaseModel b9132a3f-0ffd-49df-950d-7b257dcddbc7

        Args:
            arg (str): The name of the class and id, separated by space.

        """

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
        """
        Prints all string representation of all instances
        based or not on the class name.

        Use: all <class name> (optional)
        Ex: all              # This prints all instances of all classes
            all BaseModel    # This prints all instances of BaseModel

        Args:
            arg (str): Name of the class

        """

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
        """
        Updates an instance based on the class name, id and attributes.

        Use: update <class name> <id> <attribute name> "<attribute value>"
        Ex: update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"

        Args:
            arg (str): The name of the class, id, attrubute and
                       value separated by space.

        """

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

        """
        Verify if attribute exists, else assign actual_value as
        input argument
        """
        try:
            actual_value = getattr(obj_storage, args_list[2])
        except AttributeError:
            actual_value = args_list[3]

        # cast value to attribute type
        new_value = type(actual_value)(args_list[3])

        setattr(obj_storage, args_list[2], new_value)
        storage.save()

    def count(self, arg):
        """
        Count and prints all instance off a class name.

        Use: count(<class name>)
        Ex: count(arg) where arg is User class ("User")

        Args:
            arg (str): The name of the class

        """

        args_list = arg.split(".")
        count = 0
        for i in storage.all().items():
            if type(i[1]).__name__ == args_list[0]:
                count += 1
        print(count)

    def default(self, arg):
        """
        execute when command doesnt exist.
        Ex: User.count() its not do_XXX funtion, then default logical
            is excecuted and eval if it is count instance requirement.
        Ex: User.all() its not do_XXX funtion, then default logical
            is excecuted and eval if it is all display user instance
            requirement.
        Args: string could be <class name>.funcion where function referes to
              an expecific propose(see Ex.)
        """
        met = arg.split(".")
        if len(met) > 1:
            if met[1] == "count()":
                self.count(arg)
            if met[1] == "all()":
                eval("self.do_all(met[0])")
            if "show" in met[1]:
                id = met[1].split('(', 1)[1].split(')')[0]
                argconsole = met[0] + " " + id
                print(argconsole)
                eval("self.do_show(argconsole)")
            if "destroy" in met[1]:
                id = met[1].split('(', 1)[1].split(')')[0]
                argconsole = met[0] + " " + id
                print(argconsole)
                eval("self.do_destroy(argconsole)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
