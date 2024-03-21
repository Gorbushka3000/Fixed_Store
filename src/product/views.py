from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .dependens import get_product_by_id
from . import crud
from .shemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from src.database import db_control

router = APIRouter(tags=["Products"], prefix='/product')


@router.get('/', response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.get_products(session=session)


@router.get('/{product_id}/', response_model=Product)
async def get_product(
        product: Product = Depends(get_product_by_id)):
    return product


@router.post('/', response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, session: AsyncSession = Depends(db_control.session_dependency)):
    return await crud.create_product(session, product=product)


# @router.patch('/{product_id}', response_model=Product, status_code=status.HTTP_202_ACCEPTED)
# async def update_product(product: ProductCreate, session: AsyncSession = Depends(db_control.session_dependency)):
# qwery_product = Depends(src.product.dependens)
@router.patch('/{product_id}', response_model=Product, status_code=status.HTTP_202_ACCEPTED)
async def update_product(
        productUpdate: ProductUpdatePartial,
        product: Product = Depends(get_product_by_id),
        session: AsyncSession = Depends(db_control.session_dependency),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_up=productUpdate,
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
