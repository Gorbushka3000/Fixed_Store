from typing import Annotated

from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import db_control
from . import crud


async def get_user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_control.session_dependency)):
    product = await crud.get_user(session=session, user_id=user_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Product {user_id} not found!'
    )