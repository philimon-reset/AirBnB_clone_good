#!/usr/bin/python3
"""
    contains City class to represent a city
"""

from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """ City class """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
