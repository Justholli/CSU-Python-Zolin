from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Good(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    manufacturerId = Column(Integer, ForeignKey("manufacturer.id"))
    price = Column(Float)


class Storage(Base):
    __tablename__ = "Storage"

    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    goodId = Column(Integer, ForeignKey("good.id"))



class Manufacturer(Base):
    __tablename__ = "Manufacturer"

    manufacturerId = Column(Integer, primary_key=True, index=True)
    prName = Column(String)
    country = Column(String)


class Size(Base):
    __tablename__ = "Sizes"

    id = Column(Integer, primary_key=True)
    goodId = Column(Integer, ForeignKey("good.id"))
    size = Column(Float)
