from typing import TYPE_CHECKING

from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .models.user import User


class UserMixin:
    _id_unique: bool = False
    _back_populates: str | None = None
    _id_nullable: bool = False
    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey('user.id'),
            unique=cls._id_unique)

    @declared_attr
    def user_relationship(cls) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=cls._back_populates)
