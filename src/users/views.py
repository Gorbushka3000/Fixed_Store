from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .dependens import get_user_by_id
from . import crud
from .shemas import User, User_create, User_update
from src.database import db_control

router = APIRouter(tags=["Products"], prefix='/product')


@router.get('/', response_model=list[User])
async def get_products(session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.get_products(session=session)


@router.get('/{product_id}/', response_model=User)
async def get_product(
        user: User = Depends(get_user_by_id)):
    return user


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_product(user: User_create, session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.create_product(session, product=user)


w @ router.patch('/{product_id}', response_model=User, status_code=status.HTTP_202_ACCEPTED)


async def update_product(
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


@router.delete('/{product}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: Product = Depends(get_product_by_id),
        session: AsyncSession = Depends(db_control.session_dependency),
) -> None:
    await crud.delete_product(
        session=session,
        product=product, )
