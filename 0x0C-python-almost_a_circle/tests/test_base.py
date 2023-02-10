#!/usr/bin/python3
'''unittest file for base model'''
import unittest
from models.base import Base


class TestBaseModule(unittest.TestCase):
    '''the test class'''

    def setUp(self):
        self.base_obj1 = Base(test=True)
        self.base_obj2 = Base(25, test=True)
        self.base_obj3 = Base(test=True)

    def tearDown(self):
        del self.base_obj1
        del self.base_obj2
        del self.base_obj3

    def test_init(self):
        self.assertEqual(self.base_obj1.id, 1)
        self.assertEqual(self.base_obj2.id, 25)
        self.assertEqual(self.base_obj3.id, 2)
