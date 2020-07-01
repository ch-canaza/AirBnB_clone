#!/usr/bin/python3
'''Test for BaseModel'''
import models
from models.base_model import BaseModel
import unittest


class TestBase_Model(unittest.TestCase):
    '''start test case'''

    def setUp(cls):
        '''set the variables'''
        cls.v1 = BaseModel()
        cls.v2 = BaseModel()

    def testId(self):
        ''' test of id '''
        self.assertNotEqual(self.v1.id, self.v2.id)

    def test_datetime(self):
        ''' test for the updated_at '''
        save1 = BaseModel()
        first_updated = save1.updated_at
        save1.save()
        second_updated = save1.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_str(self):
        ''' test for str '''
        st1 = BaseModel()
        _dict = st1.__dict__
        string1 = "[BaseModel] ({}) {}".format(st1.id, _dict)
        string2 = str(st1)
        self.assertEqual(string1, string2)

    """def test_to_dict(self):
        '''here we do a test for a dict'''
        dict1 = BaseModel()
        the_dict1 = dict1.to_dict()
        self.assertIsInstance(the_dict1, dict)
        for key, value in the_dict1.items():
            count = 0
            if the_dict1['__class__'] == 'BaseModel':
                count += 1
            self.assertTrue(count == 1)
        for key, value in the_dict1.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'update_at':
                self.assertIsInstance(value, str)"""
