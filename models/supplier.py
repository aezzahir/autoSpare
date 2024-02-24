#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Supplier(BaseModel, Base):
    __tablename__ = 'suppliers'
    Noun = Column(String(128), nullable=False)
    Cage_code = Column(String(128), nullable=False)
    Adress = Column(String(128), nullable=False)
