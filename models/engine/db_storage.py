#!/usr/bin/python3
"""
database storage module
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """init"""

        try:
            self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'.
                format(
                   getenv('HBNB_MYSQL_USER'),
                   getenv('HBNB_MYSQL_PWD'),
                   getenv('HBNB_MYSQL_HOST'),
                   getenv('HBNB_MYSQL_DB')
                ),
                pool_pre_ping=True
            )
            if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)
        except:
            pass

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        return: return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object
        """

        d = {}

        if cls:
            obj = self.__session.query(cls).all()
        else:
            mycls = ['State', 'City', 'User', 'Place', 'Amenity', 'Review']
            obj = []
            for namecls in mycls:
                for o in self.__session.query(eval(namecls)):
                    obj.append(o)
        for item in obj:
            k = type(item).__name__ + '.' + str(item.id)
            d[k] = item
        return d

    def reload(self):
        """ stablish a session"""
        Base.metadata.create_all(self.__engine)
        S = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )
        self.__session = S()

    def new(self, obj):
        """  add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commits (persists) those changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj"""
        if obj:
            self.__session.delete(obj)

