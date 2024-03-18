from sqlalchemy import Column, String, Integer

from src.database.base import Base


class Product(Base):
    name = Column(String, nullable = False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)