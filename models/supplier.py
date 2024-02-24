#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Supplier(BaseModel, Base):
    __tablename__ = 'suppliers'
    name = Column(String(128), nullable=False)
    cage_code = Column(Integer, nullable=False)
    address = Column(String(128), nullable=False)
    spears = relationship("Spear", back_populates="supplier")
