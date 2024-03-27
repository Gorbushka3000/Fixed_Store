from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.database.mixins import UserMixin


class Profile(UserMixin, Base):
    _id_unique = True
    _back_populates = 'profile'

    first_name: Mapped[str] = mapped_column(String(32), nullable=False)
    last_name: Mapped[str] = mapped_column(String(32), nullable=False)
    bio: Mapped[str] = mapped_column(String(200), unique=True)
