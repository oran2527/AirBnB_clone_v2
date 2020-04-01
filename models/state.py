#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"

    name = Column(
        String(128),
        nullable=False
    )

    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship(
            'City',
            cascade='all, delete-orphan',
            backref='state',
        )
    else:
        @property
        def cities(self):
            mycities = []
            for id, c in models.storage.all(City).item():
                if self.id == c.state.id:
                    mycities.append(c)
            return mycities
