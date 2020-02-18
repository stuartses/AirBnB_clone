#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """ Class: TestBase : to test class Amenity
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(amenity.__doc__) > 0)
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = Amenity()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dictMethod(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = Amenity()
        AmenityDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'Amenity')
        self.assertIsInstance(AmenityDict['created_at'], str)
        self.assertIsInstance(AmenityDict['updated_at'], str)
        self.assertIsInstance(AmenityDict['id'], str)

    def test_hasmethods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = Amenity()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = Amenity()
        self.assertTrue(hasattr(z, "name"))
        self.assertTrue( "id" in z.__dict__)
        self.assertTrue( "created_at" in z.__dict__)
        self.assertTrue( "updated_at" in z.__dict__)


    def test_pep8(self):
        """ Function: test_pep8
                      to test if pep8 its ok to amenity.py
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_init(self):
        """ Function: test_init
                      to test Amenity Class
        """
        w = Amenity()
        self.assertTrue(isinstance(w, Amenity))
        self.assertIsInstance(w, Amenity)

    def test_str(self):
        z = Amenity()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_types(self):
        i = Amenity()
        self.assertEqual(type(i.name), str)

    def test_inherit(self):
        j = Amenity()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)



if __name__ == "__main__":
    unittest.main()
