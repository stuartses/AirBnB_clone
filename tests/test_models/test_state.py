#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models import state
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """ Class: State : to test class State
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(state.__doc__) > 0)
        self.assertTrue(len(State.__doc__) > 0)

    def test_saveMethond(self):
        """ Function: test_saveMethond
                      to test save instance methond
        """
        new_st = State()
        new_st.save()
        self.assertNotEqual(new_st.created_at, new_st.updated_at)

    def test_to_dicMethod(self):
        """ Function: test_to_dictMethod
                      to test to_dict method
        """
        new_stdic = State()
        state_dict = new_stdic.to_dict()
        self.assertEqual(new_stdic.__class__.__name__, "State")
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertIsInstance(state_dict['id'], str)

    def test_hasmethods(self):
        """ Function: test_hasmethods
                      to test if it has all basic attrbs
                      from baseModel
        """
        new_st = State()
        self.assertTrue(hasattr(new_st, "__init__"))
        self.assertTrue(hasattr(new_st, "__str__"))
        self.assertTrue(hasattr(new_st, "save"))
        self.assertTrue(hasattr(new_st, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasatribs
            to test if it has attributes
        """
        new_stattr = State()
        self.assertTrue(hasattr(new_stattr, "name"))
        self.assertTrue(hasattr(new_stattr, "created_at"))
        self.assertTrue(hasattr(new_stattr, "updated_at"))
        self.assertTrue(hasattr(new_stattr, "id"))
        self.assertTrue("id" in new_stattr.__dict__)

    def test_type(self):
        """
        """
        new_sttype = State()
        self.assertEqual(type(new_sttype.name), str)

    def test_pep8(self):
        """ Function: test_pep8
            to test if it pass PEP8 style
        """
        style = pep8.StyleGuide(quit=True)
        style_check = style.check_files(['models/state.py'])
        self.assertEqual(style_check.total_errors, 0, "fix pep8")

    def test_inherit(self):
        j = State()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
