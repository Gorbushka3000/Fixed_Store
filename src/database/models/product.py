from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database.base import Base


class Product(Base):
    name = Column(String, nullable = False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship('User', back_populates='user')