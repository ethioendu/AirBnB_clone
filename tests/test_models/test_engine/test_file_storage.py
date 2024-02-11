#!/usr/bin/python3
"""test for file storage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
        self.base_model.save()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(new_model.id), all_objects)

    def test_save_and_reload(self):
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)

if __name__ == '__main__':
    unittest.main()
