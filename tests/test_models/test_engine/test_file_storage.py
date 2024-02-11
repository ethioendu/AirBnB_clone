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

    def test_save_existing_object(self):
        self.base_model.name = "Test Model"
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        loaded_model = new_storage.all()['BaseModel.{}'.format(self.base_model.id)]
        self.assertEqual(loaded_model.name, "Test Model")

    def test_save_multiple_objects(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        base_model3 = BaseModel()
        base_model1.name = "Model 1"
        base_model2.name = "Model 2"
        base_model3.name = "Model 3"
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn('BaseModel.{}'.format(base_model1.id), all_objects)
        self.assertIn('BaseModel.{}'.format(base_model2.id), all_objects)
        self.assertIn('BaseModel.{}'.format(base_model3.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'.format(base_model1.id)].name
                         , "Model 1")
        self.assertEqual(all_objects['BaseModel.{}'.format(base_model2.id)].name
                         , "Model 2")
        self.assertEqual(all_objects['BaseModel.{}'.format(base_model3.id)].name
                         , "Model 3")

if __name__ == '__main__':
    unittest.main()
