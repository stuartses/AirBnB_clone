#!/usr/bin/python3
"""
IVAN:Unittest for City class
"""
import unittest
from models import city
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """ Class: TestBase : to test class City
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(city.__doc__) > 0)
        self.assertTrue(len(City.__doc__) > 0)

    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = City()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dictMethod(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = City()
        CityDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'City')
        self.assertIsInstance(CityDict['created_at'], str)
        self.assertIsInstance(CityDict['updated_at'], str)
        self.assertIsInstance(CityDict['id'], str)

    def test_hasmethods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = City()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = City()
        self.assertTrue(hasattr(z, "name"))
        self.assertTrue(hasattr(z, "state_id"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_pep8(self):
        """ Function: test_pep8
                      to test if pep8 its ok to user.py
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_init(self):
        """ Function: test_init
                      to test CityClass
        """
        w = City()
        self.assertTrue(isinstance(w, City))
        self.assertIsInstance(w, City)

    def test_str(self):
        z = City()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_types(self):
        i = City()
        self.assertEqual(type(i.name), str)
        self.assertEqual(type(i.state_id), str)

    def test_inherit(self):
        j = City()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
