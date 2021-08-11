#!/usr/bin/python3
"""
module containing DBStorage used for DataBase storage
"""
from sqlalchemy import create_engine
from sqlalchemy.engine import base
from sqlalchemy.orm import sessionmaker, scoped_session

from os import environ, error

from models.base_model import Base
import models

HBNB_ENV = environ.get("HBNB_ENV")
HBNB_MYSQL_USER = environ.get("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = environ.get("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = environ.get("HBNB_MYSQL_HOST")
HBNB_MYSQL_DB = environ.get("HBNB_MYSQL_DB")


class DBStorage:
    """
        class for DataBase storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)

        if (HBNB_ENV == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
            Query the current session and list all instances of cls, or all instances
        """
        result = {}
        if cls:
            for row in self.__session.query(cls).all():
                result.update({"{}.{}".format(cls.__name__, row.id):row})
        else:
            for table in Base.metadata.tables:
                cls = models.dummy_tables[table]    
                for row in self.__session.query(cls).all():
                    result.update({"{}.{}".format(cls.__name__, row.id):row})
        return result

    def new(self, obj):
        """
            add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
            create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
