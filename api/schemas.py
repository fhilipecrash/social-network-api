from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str | None = None


class PostCreate(PostBase):
    user_id: int


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class PostWithUserId(Post):
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

    class Config:
        orm_mode = True


class UserWithPosts(User):
    posts: list[Post] = []

    class Config:
        orm_mode = True
