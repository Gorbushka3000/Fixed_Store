from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import Product
from .shemas import ProductCreate, ProductUpdate, ProductDelete, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product: ProductCreate) -> Product | None:
    product = Product(**product.model_dump())
    session.add(product)
    await session.commit()
    return product


async def update_product(
        session: AsyncSession,
        product: Product,
        product_up: ProductUpdatePartial,
        partial: bool = False) -> Product:
    for name, value in product_up.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
        session: AsyncSession,
        product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
