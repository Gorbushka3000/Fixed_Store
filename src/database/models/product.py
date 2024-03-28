from typing import TYPE_CHECKING
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base
from src.database.mixins import UserMixin

if TYPE_CHECKING:
    from src.database import Like


class Product(UserMixin, Base):
    _back_populates = 'product'

    name: Mapped[str] = mapped_column(String(32), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    likes: Mapped[list["Like"]] = relationship(
        secondary="like_product_association",
        back_populates="orders",
    )
