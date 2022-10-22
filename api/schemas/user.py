from pydantic import BaseModel
from api.schemas.post import Post


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserWithPosts(User):
    posts: list[Post] = []

    class Config:
        orm_mode = True
