from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    name: str
    surname: str
    phonenumber: int


class User_get(User):
    model_config = ConfigDict(from_attributes=True)
    id: int


class User_create(User):
    pass


class User_delete(User):
    pass


class User_update(User):
    id: int | None = None
    name: str | None = None
    surname: str | None = None
    phonenumber: int | None = None
