#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    testing file storage
    """
    @classmethod
    def setUpClass(cls):
        """
        set storage variable to test
        """
        cls.storage = FileStorage()

    def test_pep8(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """
        test return dictionary __objects
        """
        storage = FileStorage()
        dictionary = storage.all()
        self.assertIsNotNone(dictionary)
        self.assertEqual(type(dictionary), dict)
        self.assertIs(dictionary, storage._FileStorage__objects)

    def test_new(self):
        """
        test if saves object into dictionary
        """
        storage = FileStorage()
        dictionary = storage.all()
        x = User()
        x.id = 31416
        x.name = "Pi"
        storage.new(x)
        key = x.__class__.__name__ + "." + str(x.id)
        self.assertIsNotNone(dictionary[key])

    def test_reload(self):
        """
        test if reloads objects from json file in dictionary
        """
        self.storage.save()
        path = os.path.dirname(os.path.abspath("console.py"))
        fd = os.path.join(path, "file.json")
        with open(fd, 'r') as f:
            lines = f.readlines()

        try:
            os.remove(pt)
        except BaseException:
            pass

        self.storage.save()

        with open(fd, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(pt)
        except BaseException:
            pass

        with open(fd, "w") as f:
            f.write("{}")
        with open(fd, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")

        self.assertIs(self.storage.reload(), None)

if __name__ == "__main__":
    unittest.main()
