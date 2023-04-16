#!/usr/bin/python3
"""
This script similar to model_state.py named model_city.py
that contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """Class that represents a city"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id

    def __str__(self):
        return "{}: {}".format(self.id, self.name)
