#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Spear(BaseModel, Base):
    __tablename__ = 'spears'
    Noun = Column(String(128), nullable=False)
    NSN = Column(String(128), nullable=False)
    Description = Column(String(128), nullable=False)
    suppliers = relationship("Supplier", backref="spears")
