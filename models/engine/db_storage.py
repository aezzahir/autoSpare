#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.spear import Spear  # Import the Spear class
from models.user import User
from models.supplier import Supplier
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Spear": Spear, "BaseModel": BaseModel, "Supplier": Supplier, "User": User}


class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        SPEAR_MYSQL_USER = getenv('SPEAR_MYSQL_USER')
        SPEAR_MYSQL_PWD = getenv('SPEAR_MYSQL_PWD')
        SPEAR_MYSQL_HOST = getenv('SPEAR_MYSQL_HOST')
        SPEAR_MYSQL_DB = getenv('SPEAR_MYSQL_DB')
        SPEAR_ENV = getenv('SPEAR_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(SPEAR_MYSQL_USER,
                                             SPEAR_MYSQL_PWD,
                                             SPEAR_MYSQL_HOST,
                                             SPEAR_MYSQL_DB))
        if SPEAR_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        A method to retrieve one object
        """
        return self.all(cls).get(f"{cls.__name__}.{id}")

    def count(self, cls=None):
        """
        A method to count the number of objects in storage
        """
        return len(self.all(cls))
    
    def get_session(self):
        """Get the current database session"""
        return self.__session
