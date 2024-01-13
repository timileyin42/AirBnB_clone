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
        d = {"name": "My First Model"}
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

    def test_correct_classattr(self):
        """ Checks if class attr are present """
        b = User()
        attr = ["email", "password", "first_name", "last_name"]
        d = b.__dict__
        for i in attr:
            self.assertFalse(i in d)
            self.assertTrue(hasattr(b, i))
            self.assertEqual(getattr(b, i, False), "")

    def test_set_attr(self):
        """ Check settings instance attr and accessing class attr """
        b = User()
        attr = ["email", "password", "first_name", "last_name"]
        value = ["ibro@gmail.com", "password", "fikri", "page"]
        for i, j in zip(attr, value):
            setattr(b, i, j)
        d = b.__dict__
        for i, j, in zip(attr, value):
            self.assertEqual(getattr(b, i, False), j)
        for i in attr:
            self.assertEqual(getattr(b.__class__, i, False), "")


class Test_initUser(unittest.TestCase):
    """ Class for unittest of __init__ """

    def setUp(self):
        """ set up for all methods """
        pass

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation_no_arg(self):
        """ No arguments """
        b1 = User()
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_attr_types(self):
        """ No arguments """
        b1 = User()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_id_diff_for_each_instance(self):
        """  Checks if every id generated is different """
        b1 = User()
        b2 = User()
        b3 = User()
        b4 = User()
        self.assertFalse(b1.id == b2.id)
        self.assertFalse(b1.id == b3.id)
        self.assertFalse(b1.id == b4.id)
        self.assertFalse(b2.id == b3.id)
        self.assertFalse(b2.id == b4.id)
        self.assertFalse(b3.id == b4.id)

    " =========================== ARGS ========================= "

    def test_args(self):
        """ Tests that args works """
        b1 = User(1)
        b2 = User(1, "good")
        b3 = User(1, "good", (1, 2))
        b4 = User(1, "good", (1, 2), [1, 2])

    def test_args_def_(self):
        """ Tests that defaults attr are set even with args """
        b1 = User(1, "good", (1, 2), [1, 2])
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

    " =========================== KWARGS =========================== "

    def test_instance_creation_kwarg(self):
        """ Arguments in kwarg """
        d = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
             'created_at': '2017-09-28T21:05:54.119427',
             '__class__': 'User',
             'updated_at': ' 2017-09-28T21:05:54.119572'}
        b1 = User(**d)
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))
        self.assertTrue(b1.__class__ not in b1.__dict__)

        self.assertEqual(b1.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertEqual(b1.created_at.isoformat(),
                         '2017-09-28T21:05:54.119427')
        self.assertEqual(b1.updated_at.isoformat(),
                         '2017-09-28T21:05:54.119572')

    def test_no_default_args(self):
        """ Checks if id and the dates are created even if not in kwargs """
        d = {"name": "My First Model"}
        b1 = User(**d)
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertEqual(b1.name, "My First Model")
