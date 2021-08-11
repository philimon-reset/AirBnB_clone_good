#!/usr/bin/python3
"""
    module containing place
"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.sql.schema import ForeignKey


class Place(BaseModel, Base):
    """
        Place class
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
