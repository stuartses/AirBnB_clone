#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models import place
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """ Class: TestBase : to test class Place
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(place.__doc__) > 0)
        self.assertTrue(len(Place.__doc__) > 0)

    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = Place()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dictMethod(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = Place()
        PlaceDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'Place')
        self.assertIsInstance(PlaceDict['created_at'], str)
        self.assertIsInstance(PlaceDict['updated_at'], str)
        self.assertIsInstance(PlaceDict['id'], str)

    def test_hasmethods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = Place()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = Place()
        self.assertTrue(hasattr(z, "city_id"))
        self.assertTrue(hasattr(z, "user_id"))
        self.assertTrue(hasattr(z, "name"))
        self.assertTrue(hasattr(z, "description"))
        self.assertTrue(hasattr(z, "number_rooms"))
        self.assertTrue(hasattr(z, "number_bathrooms"))
        self.assertTrue(hasattr(z, "number_bathrooms"))
        self.assertTrue(hasattr(z, "price_by_night"))
        self.assertTrue(hasattr(z, "latitude"))
        self.assertTrue(hasattr(z, "longitude"))
        self.assertTrue(hasattr(z, "amenity_id"))
        self.assertTrue(hasattr(z, "created_at"))
        self.assertTrue(hasattr(z, "updated_at"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_pep8(self):
        """ Function: test_pep8
                      to test if pep8 its ok to place.py
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_init(self):
        """ Function: test_init
                      to test Place Class
        """
        w = Place()
        self.assertTrue(isinstance(w, Place))
        self.assertIsInstance(w, Place)

    def test_str(self):
        z = Place()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_strings(self):
        i = Place()
        self.assertEqual(type(i.city_id), str)
        self.assertEqual(type(i.user_id), str)
        self.assertEqual(type(i.name), str)
        self.assertEqual(type(i.description), str)
        self.assertEqual(type(i.number_rooms), int)
        self.assertEqual(type(i.number_bathrooms), int)
        self.assertEqual(type(i.max_guest), int)
        self.assertEqual(type(i.price_by_night), int)
        self.assertEqual(type(i.latitude), float)
        self.assertEqual(type(i.longitude), float)
        self.assertEqual(type(i.amenity_id), list)

    def test_inherit(self):
        j = Place()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
