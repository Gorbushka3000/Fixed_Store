from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.database import Base

if TYPE_CHECKING:
    from src.database import Product


class User(Base):
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    surname: Mapped[str] = mapped_column(String(32), nullable=False)
    phone: Mapped[str] = mapped_column(String(32), unique=True)
    product: Mapped[list['Product']] = relationship(back_populates='user')
