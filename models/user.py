#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import LoginManager, login_user, UserMixin


class User(BaseModel, Base, UserMixin):
    __tablename__ = 'users'
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(60), nullable=False)
    purchased_items = relationship("Spear", backref="buyer_user", lazy="joined")