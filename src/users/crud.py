from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import User
from .shemas import User_create, User_update


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    user = result.scalars().all()
    return list(user)


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user: User_create) -> User | None:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    return user


async def update_user(
        session: AsyncSession,
        user: User,
        user_up: User_update,
        partial: bool = False) -> User:
    for name, value in user_up.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user