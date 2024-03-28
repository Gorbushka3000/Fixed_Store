from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.database.mixins import UserMixin

if TYPE_CHECKING:
    from src.database import Product, LikeProductAssociation


class Like(UserMixin, Base):
    _back_populates = 'product'

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow()
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="like_product_association ",
        back_populates="likes",
    )

    products_details: Mapped[list["LikeProductAssociation"]] = relationship(
        back_populates='like'
    )

