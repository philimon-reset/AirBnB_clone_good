#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ City class """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id))
    name = Column(String(128), nullable=False)
