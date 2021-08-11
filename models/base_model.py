#!/usr/bin/python3
"""
    Module containing BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel():
    """
        Base class to define all common attributes and methods for
        other classes
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

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
                                     self.id, self.__dict__)

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
        custom_dict.update({"__class__": self.__class__.__name__})
        for key in list(self.__dict__):
            if key in ("created_at", "updated_at"):
                custom_dict.update({key: getattr(self, key).isoformat()})
            elif key == "_sa_instance_state":
                self.__dict__.pop(key)
            else:
                custom_dict.update({key: getattr(self, key)})
        return custom_dict

    def delete(self):
        """ delete the current instance from the storage
        """
        k = "{}.{}".format(type(self).__name__, self.id)
        del models.storage.__objects[k]
