#!/usr/bin/python3
"""
update
"""
import json

from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name = obj_dict['__class__']
                    obj = globals()[class_name](**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
    
    def serialize(self, obj):
        """Serialize an object to JSON format."""
        if isinstance(obj, (Place, State, City, Amenity, Review)):
            return obj.to_dict()
        return obj
    
    def deserialize(self, json_dict):
        """Deserialize a JSON dictionary to an object."""
        if '__class__' in json_dict:
            class_name = json_dict['__class__']
            if class_name == 'Place':
                return Place(**json_dict)
            elif class_name == 'State':
                return State(**json_dict)
            elif class_name == 'City':
                return City(**json_dict)
            elif class_name == 'Amenity':
                return Amenity(**json_dict)
            elif class_name == 'Review':
                return Review(**json_dict)
        return json_dict
