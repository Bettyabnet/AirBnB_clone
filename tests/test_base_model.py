#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        model = BaseModel()
        self.assertEqual(model.my_number, 89)
        self.assertEqual(model.name, 'My First Model')

    def test_str_method(self):
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()

        expected_created_at = model.created_at.isoformat()
        actual_created_at = model_dict['created_at']

        self.assertEqual(actual_created_at, expected_created_at)

        # Print the desired output
        print(f"[BaseModel] ({model.id}) {model.__dict__}")
        print(f"[BaseModel] ({model.id}) {model.__dict__}")
        print(json.dumps(model_dict, sort_keys=True, indent=4))
        print("JSON of my_model:")
        for key, value in model_dict.items():
            print(f"    {key}: ({type(value)}) - {value}")


if __name__ == '__main__':
    unittest.main()
