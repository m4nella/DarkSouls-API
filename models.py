from sqlalchemy import Boolean, Column, Integer, String 
from database import Base

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    level = Column(Integer)
    class_name = Column(String(50))
    starting_gift = Column(String(50))
    covenant = Column(String(50))

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    type = Column(String(50))
    description = Column(String(100))
    required_level = Column(Integer)
    required_class = Column(String(50))