#!/usr/bin/python3
"""Contains tests for BaseModel class"""

import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle
import inspect
from models.base_model import BaseModel
import models

class TestDocsBaseModel(unittest.TestCase):
    """Tests for presence of BaseModel class documentation"""

    @classmethod
    def setUpClass(cls):
        """Easy access to all BaseModel functions"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for presence of module documentation"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for presence of BaseModel class documentation"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for presence of documentation in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """Checks that base_model complies with PEP 8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks that test_base_model complies with PEP 8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_basemodel(unittest.TestCase):
    """Testing the Base module"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.base = BaseModel()
        cls.base.name = 'BaseModel'
        cls.base.value = BaseModel

    @classmethod
    def tearDownClass(cls):
        """ tear down class at end of testing """
        del cls.base

    def test_default(self):
        """ """
        i = self.base.value()
        self.assertEqual(type(i), self.base.value)

    def test_kwargs(self):
        """Testing normal acceptance of kwargs"""
        i = self.base.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Testing handling of a kwarg as an int"""
        i = self.base.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing save"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_str(self):
        """Testing __str__"""
        i = self.base.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.base.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Testing to_dict"""
        i = self.base.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Testing handling of no kwargs being supplied"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.base.value(**n)

    @unittest.skip
    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.base.value(**n)

    def test_id(self):
        """Testing that a string-based id is created"""
        new = self.base.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Testing that attribute created_at is correct"""
        new = self.base.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Testing that attribute updated_at is correct"""
        new = self.base.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    @unittest.skipIf(models.storage_type == "db", "test not applicable")
    def test_delete(self):
        """Testing delete method"""
        self.base.delete()
        self.assertNotIn(self.base, models.FileStorage)

