#!/usr/bin/python3
""" Spear Module for our project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Spear(BaseModel, Base):
    __tablename__ = 'spears'
    designation = Column(String(128), nullable=False)
    NSN = Column(Integer, nullable=False)
    description = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    supplier_id = Column(String(60), ForeignKey('suppliers.id'))
    supplier = relationship("Supplier", back_populates="spears", lazy="joined")
