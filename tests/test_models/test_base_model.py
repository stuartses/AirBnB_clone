#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models import base_model
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """ Class: TestBase : to test class BaseModel
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(base_model.__doc__) > 0)
        self.assertTrue(len(BaseModel.__doc__) > 0)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)

    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = BaseModel()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dictMethod(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = BaseModel()
        BaseDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'BaseModel')
        self.assertIsInstance(BaseDict['created_at'], str)
        self.assertIsInstance(BaseDict['updated_at'], str)
        self.assertIsInstance(BaseDict['id'], str)

    def test_attribs(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        i = BaseModel()
        self.assertTrue(hasattr(i, "__init__"))
        self.assertTrue(hasattr(i, "__str__"))
        self.assertTrue(hasattr(i, "save"))
        self.assertTrue(hasattr(i, "to_dict"))

    def test_pep8(self):
        """ Function: test_pep8
                      to test if pep8 its ok to base_model.py
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_init(self):
        """ Function: test_init
                      to test BaseModel Class
        """
        w = BaseModel()
        self.assertTrue(isinstance(w, BaseModel))
        self.assertIsInstance(w, BaseModel)

    def test_str(self):
        z = BaseModel()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)


if __name__ == "__main__":
    unittest.main()
