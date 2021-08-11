#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City"""
        result = []
        for i in self.cities:
            if i.state_id == self.id:
                result.append(i)
        return result
