#!/usr/bin/python3
"""
    module containing user class
"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String

class User(BaseModel, Base):
    """
        User class
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship("Review", backref="user")
