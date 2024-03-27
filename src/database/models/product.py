from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.database.base import Base
from src.database.mixins import UserMixin


class Product(UserMixin, Base):
    _back_populates = 'product'

    name: Mapped[str] = mapped_column(String(32), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
