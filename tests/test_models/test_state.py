import models
from models.state import State
import os
import unittest
from models.base_model import BaseModel
"""import json"""


class TestState(unittest.TestCase):
    """we start the test"""
    
    
    def test_docstring(self):
        '''test if function, methods, classes and modules have doc
        string'''
        msj = "Module doesnt have docstring"
        obj = models.state.__doc__
        self.assertIsNotNone(obj, msj) # Modules
        msj = "Classes doesnt have docstring"
        self.assertIsNotNone(obj, msj) # Classes
        
    def test_executable_file(self):
        '''test if file has permissions u+x to executable'''
        #Check for read access
        is_read_true = os.access('models/state.py', os.R_OK)
        self.assertTrue(is_read_true)
        #check for write access
        is_write_true = os.access('models/state.py', os.W_OK)
        self.assertTrue(is_write_true)
        #Check for execution access
        is_exec_true = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_exec_true)
        
    def test_is_an_instance(self):
        '''check if my_models is an instance of BaseModel'''
        my_model = State()
        self.assertIsInstance(my_model, State)