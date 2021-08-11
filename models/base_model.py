#!/usr/bin/python3
"""
    Module containing BaseModel
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

from uuid import uuid4
from datetime import datetime
import models


Base = declarative_base()

class BaseModel():
    """
        Base class to define all common attributes and methods for
        other classes
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """
            initialization
        """
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    iso = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(kwargs[key], iso))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
            return string representation of a Model
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.to_dict())

    def save(self):
        """
            update latest updation time of a model
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            custom representation of a model
        """
        custom_dict = {}
        # custom_dict.update({"__class__": self.__class__.__name__})
        for key in self.__dict__:
            if key in ("created_at", "updated_at"):
                custom_dict.update({key: getattr(self, key).isoformat()})
            else:
                custom_dict.update({key: getattr(self, key)})
        if ("_sa_instance_state" in custom_dict):
            custom_dict.pop("_sa_instance_state")
        return custom_dict

    def delete(self):
        models.storage.delete(self)
