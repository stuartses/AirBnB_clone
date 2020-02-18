#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models import review
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """ Class: TestBase : to test class Review
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(review.__doc__) > 0)
        self.assertTrue(len(Review.__doc__) > 0)

    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = Review()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dictMethod(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = Review()
        ReviewDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'Review')
        self.assertIsInstance(ReviewDict['created_at'], str)
        self.assertIsInstance(ReviewDict['updated_at'], str)
        self.assertIsInstance(ReviewDict['id'], str)

    def test_hasmethods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = Review()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = Review()
        self.assertTrue(hasattr(z, "place_id"))
        self.assertTrue(hasattr(z, "user_id"))
        self.assertTrue(hasattr(z, "text"))
        self.assertTrue(hasattr(z, "created_at"))
        self.assertTrue(hasattr(z, "updated_at"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_pep8(self):
        """ Function: test_pep8
                      to test if pep8 its ok to review.py
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_init(self):
        """ Function: test_init
                      to test Review Class
        """
        w = Review()
        self.assertTrue(isinstance(w, Review))
        self.assertIsInstance(w, Review)

    def test_str(self):
        z = Review()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_types(self):
        i = Review()
        self.assertEqual(type(i.place_id), str)
        self.assertEqual(type(i.user_id), str)
        self.assertEqual(type(i.text), str)

    def test_inherit(self):
        j = Review()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
