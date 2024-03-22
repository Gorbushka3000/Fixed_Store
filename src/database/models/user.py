from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phoneNumber = Column(Integer, unique=True)
    user = relationship('Product', back_populates='product')