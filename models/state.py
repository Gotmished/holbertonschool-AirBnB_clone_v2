#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete"
        )
    else:
        @property
        def cities(self):
            """
            Case when FileStorage is used as storage method.
            Returning a city list where each_city.state_id ==
            current state id (states.id: foreign key)
            """
            list_cities = []
            all_cities = models.storage.all(City)
            for each_city in all_cities.values():
                if each_city.state_id == self.id:
                    list_cities.append(each_city)
            return list_cities
