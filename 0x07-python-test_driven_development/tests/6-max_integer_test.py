#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer
"""
    max_integer return the max integer of a list
"""


class TestMaxInteger(unittest.TestCase):

    def test_integer(self):
        "Test numbers cases"
        self.assertEqual(max_integer([7, 4, 5, 6, 2]), 7)
        self.assertEqual(max_integer([2, 4, 200, 6, 7]), 200)
        self.assertEqual(max_integer([-2, -4, -5, -100, 0]), 0)
        self.assertEqual(max_integer([2.3, 4.6, 5.3, 6, 32.3]), 32.3)
        self.assertEqual(max_integer([45]), 45)

    def test_void(self):
        "Test empty"
        self.assertEqual(max_integer([]), None)

    def test_raise(self):
        "Test error cases"
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, {2, 8, 9})
