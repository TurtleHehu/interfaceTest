# -*- coding:UTF-8 -*-

import unittest
from learning.mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfunc.py"""

    @classmethod
    def setUpClass(cls):
        print("do something before test.Prepare environment.")

    @classmethod
    def tearDownClass(cls):
        print("do something after test.Clean up.")

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3,add(1, 2))
        self.assertNotEqual(3,add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1,minus(3, 2))
        self.assertNotEqual(2,minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6,multi(3, 2))
        self.assertNotEqual(5,multi(3, 3))

    @unittest.skip("I do not want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2,divide(8, 4))
        self.assertNotEqual(1.5,divide(3, 2))

if __name__ =="__main__":
    unittest.main()

