import models
from models.engine.file_storage import file_storage
import unittest


class testFile_Storage(unittest.TestCase):
    """we start the test"""
    
    
    def test_docstring(self):
        '''test if function, methods, classes and modules have doc
        string'''
        msj = "Module doesnt have docstring"
        obj = models.engine.file_storage.__doc__
        self.assertIsNotNone(obj, msj) # Modules
        msj = "Classes doesnt have docstring"
        self.assertIsNotNone(obj, msj) # Classes
        
    def test_executable_file(self)