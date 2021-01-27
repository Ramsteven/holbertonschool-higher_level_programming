#!usr/bin/python3
""" test module Base"""

from inspect
from unittest import TestCase
from models.base import Base
import json


class TestBase(TestCase):
    """
    Class to check base
    """
    def test_A_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base("2").id, "2")

    def test_B_to_json_string(self):
        """
        test to_json_string
        """
        self.assertEqual(Base.to_json_string(None), [])
        self.assertEqual(Base.to_json_string([]), [])
        self.assertEqual(Base.to_json_string([{'id': 12}]),
                         json.dumps([{'id': 12}]))
        self.assertEqual(Base.to_json_string([{'id': 12}]),
                         json.dumps([{'id': 12}]))

    def test_C_from_json_string(self):
        """
        test from_json_string
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    def test_D_documentation(self):
        """
        test documentation
        """
        self.assertTrue(len(Base.__doc__) > 0)
        methods = inspect.getmembers(Base, predictive=inspect.inmethod)

        for name, method in methods:
            self.assertTrue(len(methods.__doc__) > 0)
