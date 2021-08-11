#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String


class Review(BaseModel, Base):
    """
        Review class
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), nullable=False, ForigenKey(Place.id))
    user_id = Column(String(60), nullable=False, ForigenKey(User.id))
    text = Column(String(1024), nullable=False)
