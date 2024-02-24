#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Spear(BaseModel, Base):
    __tablename__ = 'products'
    designation = Column(String(128), nullable=False)
    NSN = Column(Integer, nullable=False)
    description = Column(String(128), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship("Supplier", back_populates="spears")
