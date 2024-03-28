from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


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
