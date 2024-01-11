#!/usr/bin/python3
""" Unitest for user class
"""


from datetime import datetime
import io
from model.base_model  import BaseModel
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
        except:
            pass

    def test_instance(self):
        """ Checks if user is instance of base_model """
        b = user()
        self.assertTrue(isinstance(b, BaseModel))
