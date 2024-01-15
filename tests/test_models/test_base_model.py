#!/usr/bin/python3
""" Unittest for BaseModel class
"""

from datetime import datetime
import io
from models.base_model import BaseModel
from os import path, remove
import unittest
from unittest.mock import patch
from time import sleep


class Test_init(unittest.TestCase):
    """ Class for unittest of __init__ """

    def setUp(self):
        """ Set up for all methods """
        pass

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation_no_arg(self):
        """ No arguments """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_attr_types(self):
        """ No arguments """
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_id_diff_for_each_instance(self):
        """ Checks If every id generated is different """
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        b4 = BaseModel()
        self.assertFalse(b1.id == b2.id)
        self.assertFalse(b1.id == b3.id)
        self.assertFalse(b1.id == b4.id)
        self.assertFalse(b2.id == b3.id)
        self.assertFalse(b2.id == b4.id)
        self.assertFalse(b3.id == b4.id)

    " ===========================  ARGS  ================================"

    def test_args(self):
        """ Tests that args works """
        b1 = BaseModel(1)
        b2 = BaseModel(1, "good")
        b3 = BaseModel(1, "good", (1, 2))
        b4 = BaseModel(1, "good", (1, 2), [1, 2])

    def test_args_def_(self):
        """ Tests that default attr are set even with args """
        b1 = BaseModel(1, "good", (1, 2), [1, 2])
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

    " =========================== KWARGS  =============================== "

    def test_instance_creation_kwarg(self):
        """ Arguments in Kwarg """
        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
             'created_at': '2017-09-28T21:03:54.052298',
             '__class__': 'BaseModel',
             'updated_at': '2017-09-28T21:03:54.052302'}
        b1 = BaseModel(**d)
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))
        self.assertTrue(b1.__class__ not in b1.__dict__)

        self.assertEqual(b1.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(b1.created_at.isoformat(),
                         '2017-09-28T21:03:54.052298')
        self.assertEqual(b1.updated_at.isoformat(),
                         '2017-09-28T21:03:54.052302')

    def test_no_default_args(self):
        """ Checks if id and dates are created even if not in kwargs """
        d = {"name": "Holberton"}
        b1 = BaseModel(**d)
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertEqual(b1.name, "My_First_Model")

    def test_dates_str_to_datetime(self):
        """ Checks that the proper conversion is made for datetimes """

        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
             'created_at': '2017-09-28T21:03:54.052298',
             '__class__': 'BaseModel',
             'updated_at': '2017-09-28T21:03:54.052302'}
        b1 = BaseModel(**d)
        self.assertEqual(b1.created_at.isoformat(),
                         '2017-09-28T21:03:54.052298')
        self.assertEqual(b1.updated_at.isoformat(),
                         '2017-09-28T21:03:54.052302')
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_args_kwargs(self):
        """ Tests that kwargs works even if there is args """

        d = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
             'created_at': '2017-09-28T21:05:54.119427',
             '__class__': 'BaseModel',
             'updated_at': '2017-09-28T21:05:54.119572'}
        b1 = BaseModel(1, "Hello", ["World"], **d)
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


class Test_str__(unittest.TestCase):

    """ Class for testing __str__ method """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_print(self):
        """ Tests the __str__ method """
        b1 = BaseModel()
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)

    def test_print2(self):
        """ Tests the __str__ method 2"""
        b1 = BaseModel()
        b1.name = "'My First Model"
        b1.code = 123
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)

    def test_print_args(self):
        """ Test __str__ with args """
        b1 = BaseModel(None, 1, ["A"])
        b1.name = "'My First Model"
        b1.code = 123
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)

    def test_print_kwargs(self):

        """ Test __str__ with prev set kwargs """
        d = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
             'created_at': '2017-09-28T21:05:54.119427',
             '__class__': 'BaseModel',
             'updated_at': '2017-09-28T21:05:54.119572'}
        b1 = BaseModel(**d)
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)
