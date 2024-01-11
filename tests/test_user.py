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

class tyest_instanceUser(unittest.testCase):
