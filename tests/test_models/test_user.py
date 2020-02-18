#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models import user
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """ Class: TestBase : to test class User
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(user.__doc__) > 0)
        self.assertTrue(len(User.__doc__) > 0)

    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = User()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dictMethod(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = User()
        UserDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'User')
        self.assertIsInstance(UserDict['created_at'], str)
        self.assertIsInstance(UserDict['updated_at'], str)
        self.assertIsInstance(UserDict['id'], str)

    def test_hasmethods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = User()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = User()
        self.assertTrue(hasattr(z, "email"))
        self.assertTrue(hasattr(z, "password"))
        self.assertTrue(hasattr(z, "last_name"))
        self.assertTrue(hasattr(z, "first_name"))
        self.assertTrue(hasattr(z, "created_at"))
        self.assertTrue(hasattr(z, "updated_at"))
        self.assertTrue( "id" in z.__dict__)
        self.assertTrue( "created_at" in z.__dict__)
        self.assertTrue( "updated_at" in z.__dict__)


    def test_pep8(self):
        """ Function: test_pep8
                      to test if pep8 its ok to user.py
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_init(self):
        """ Function: test_init
                      to test User Class
        """
        w = User()
        self.assertTrue(isinstance(w, User))
        self.assertIsInstance(w, User)

    def test_str(self):
        z = User()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_strings(self):
        i = User()
        self.assertEqual(type(i.email), str)
        self.assertEqual(type(i.password), str)
        self.assertEqual(type(i.first_name), str)
        self.assertEqual(type(i.first_name), str)

    def test_inherit(self):
        j = User()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
