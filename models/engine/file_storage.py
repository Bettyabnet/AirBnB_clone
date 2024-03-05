#!/usr/bin/python3
"""
update
"""
import json
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    # Existing code ...
    
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
