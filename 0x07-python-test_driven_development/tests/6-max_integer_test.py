#!usr/bin/pyton3
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
        self.assertEqual(max_integer([2, 4, 5, 6, 7]), 7)
        self.assertEqual(max_integer([2, 4, 200, 6, 7]), 200)
        self.assertEqual(max_integer([2, 4, 5, 100, 7]), 100)
        self.assertEqual(max_integer([2, 4, 5, 6, 323]), 323)

    def test_void(self):
        self.assertEqual(max_integer([]), None)

    def test_raise(self):
        self.assertRaises(TypeError, max_integer(), None)
        self.assertRaises(TypeError, max_integer(), 5)
        self.assertRaises(TypeError, max_integer(), {2, 8, 9})

if __name__ == '__main__':
    unittest.main()
