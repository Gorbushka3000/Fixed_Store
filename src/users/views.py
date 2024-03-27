from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .dependens import get_user_by_id
from . import crud
from .shemas import User, User_create, User_update
from src.database import db_control

router = APIRouter(tags=["Users"], prefix='/user')


@router.get('/', response_model=list[User])
async def get_users(session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.get_users(session=session)


@router.get('/{user_id}/', response_model=User)
async def get_user(
        user: User = Depends(get_user_by_id)):
    return user


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User_create, session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.create_user(session, user=user)


@router.patch('/{user_id}', response_model=User, status_code=status.HTTP_202_ACCEPTED)
async def update_user(
        userUpdate: User_update,
        user: User = Depends(get_user_by_id),
        session: AsyncSession = Depends(db_control.session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_up=userUpdate,
        partial=True,
    )


@router.delete('/{user}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        user: User = Depends(get_user_by_id),
        session: AsyncSession = Depends(db_control.session_dependency),
) -> None:
    await crud.delete_user(
        session=session,
        user=user)
