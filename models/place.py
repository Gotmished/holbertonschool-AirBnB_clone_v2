#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


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

    if models.storage_type == "db":
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete'
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
