#!/usr/bin/python3
""" Unitest for user class
"""


from datetime import datetime
import io
from model.base_model import BaseModel
from model.user import user
from os import path, remove
import unittest
from unitest.mock import patch
from time import sleeep


class Test_instanceUser(unittest.testCase):

    """ Class for unittest of instance check """

    def tearDown(self):
        """ Tear Down for all methods """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """ Checks if user is instance of base_model """
        b = user()
        self.assertTrue(isinstance(b, BaseModel))

    def test_instance_args(self):
        """ checks if user with args is instance of base_model """
        b = User(123, "Hello", ["World"])
        self.assertTrue(isinstance(b, BaseModel))

    def test_instance_kwargs(self):
        """ Checks if user with args is instance of base_model """
        d = {"name": "ALX"}
        b = User(**d)
        self.assertTrue(isinstance(b, BaseModel))

class Test_class_attrsUser(unittest.TestCase):

    """ Class for checking if class attar were set correctly """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
