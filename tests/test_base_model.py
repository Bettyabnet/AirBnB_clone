#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_str_method(self):
        """Test the __str__() method of the BaseModel class"""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {{'id': '{model.id}', 'created_at': {model.created_at}, 'updated_at': {model.updated_at}}}"
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test the save() method of the BaseModel class"""
        model = BaseModel()
        model.save()
        self.assertIsNotNone(model.updated_at)
        self.assertIsNotNone(model.created_at)

    def test_to_dict_method(self):
        """Test the to_dict() method of the BaseModel class"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
