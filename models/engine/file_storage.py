#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os.path import exists


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        cls_dict = {}
        if cls is not None:
            '''Check to see if cls exists in filestorage & add to dict.'''
            for k, v in self.__objects.items():
                if cls == v.__class__.__name__ or cls == v.__class__:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        try:
            if exists(self.__file_path):
                temp = {}
                with open(self.__file_path, "r") as f:
                    temp = json.load(f)
                    for k in temp:
                        self.__objects[k] = classes[temp[k]["__class__"]](**temp[k])
        except:
            pass

    def delete(self, obj=None):
        """Deletes an object if it exists in FileStorage"""
        if obj is not None:
            key = "{}:{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Restores objects from storage(json)"""
        self.reload()
