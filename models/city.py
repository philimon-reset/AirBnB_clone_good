#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String

class City(BaseModel, Base):
    """ City class """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
