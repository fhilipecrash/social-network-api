from typing import Union
from fastapi import FastAPI
from api import crud
from api import database

app = FastAPI()


@app.get("/users")
def get_users(email: Union[str, None] = None, with_posts: bool = False):
    if email:
        return crud.get_user_by_email(database.SessionLocal(), email)
    return crud.get_users(database.SessionLocal())


@app.get("/users/{user_id}")
def get_user(user_id: int, with_posts: bool = False):
    return crud.get_user(database.SessionLocal(), user_id)
