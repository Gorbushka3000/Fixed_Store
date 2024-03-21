from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .shemas import Product, ProductCreate
from src.database import db_control

router = APIRouter(tags=["Products"], prefix='/product')


@router.get('/', response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.get_products(session=session)


@router.get('/{product_id}/', response_model=list[Product])
async def get_product(product_id: int, session: AsyncSession = Depends(db_control.session_dependency)):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Product {product_id} not found!'
    )


@router.post('/', response_model=Product)
async def create_product(product: ProductCreate, session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.create_product(session, product=product)
