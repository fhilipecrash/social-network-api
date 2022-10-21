from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str | None = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    posts: list[Post] = []

    class Config:
        orm_mode = True
