#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """This class manages storage of hbnb models in an SQL database"""
    __engine = "None"
    __session = "None"

    def __init__(self):
        """Creating the engine"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Class-specific query on current database session"""
        cls_dict = {}
        if cls in classes:
            for obj in self.__session.query(classes[cls]).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                cls_dict[key] = obj
            return cls_dict
        else:
            for key, value in classes.items():
                for obj in self.__session.query(value).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    cls_dict[key] = obj
            return cls_dict

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits changes made to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes a specified object from the current database section"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Session = scoped_session(sessionmaker())
        Base.metadata.create_all(self.__engine)
        Session.configure(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
