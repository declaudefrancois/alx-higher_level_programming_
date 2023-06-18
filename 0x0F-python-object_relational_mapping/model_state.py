#!/usr/bin/python3
"""Instanciate a declarative base instance
   and defines a State class.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Defines a declarative Mapping class for the states table.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
