#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete'
        )
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False
        )
    else:
        @property
        def reviews(self):
            """Case when FileStorage is used as storage method"""
            list_reviews = []
            all_reviews = models.storage.all(Review)
            for each_review in all_reviews.values():
                if each_review.place_id == self.id:
                    list_reviews.append(each_review)
            return list_reviews

        @property
        def amenities(self):
            """Case when FileStorage us used as storage method"""
            list_amenities = []
            all_amenities = models.storage.all(Amenity)
            for each_amenity in all_amenities.values():
                if each_amenity.place_id == self.id:
                    list_amenities.append(each_amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """Adding Amenity.id to attribute amenity_ids"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
