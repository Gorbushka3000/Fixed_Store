from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.database import Like, Product

class LikeProductAssociation(Base):
    __tablename__ = "like_product_association"
    __table_args__ = (
        UniqueConstraint(
            'like_id',
            'product_id',
            name='idx_unique_like_product'
        )
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    like_id: Mapped[int] = mapped_column(ForeignKey('likes.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('likes.id'))
    like: Mapped["Like"] = relationship(back_populates="products_details")
    product: Mapped["Like"] = relationship(back_populates="likes_details")
