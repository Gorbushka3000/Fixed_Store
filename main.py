import uvicorn
from src.product.views import router as product_router
from src.users.views import router as user_router
from fastapi import FastAPI


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with db_control.engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield


app = FastAPI()
app.include_router(product_router)
app.include_router(user_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
