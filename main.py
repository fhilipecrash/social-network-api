from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from api import crud, schemas, database
from sqlalchemy.orm import Session

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users", response_model=list[schemas.User] | schemas.User)
def get_users(email: Union[str, None] = None, db: Session = Depends(get_db)):
    if email:
        user = crud.get_user_by_email(db, email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    return crud.get_users(db)


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/{user_id}/posts", response_model=list[schemas.PostWithUserId] | schemas.UserWithPosts)
def get_user_posts(user_id: int, with_user_info: bool = False, db: Session = Depends(get_db)):
    if with_user_info:
        user = crud.get_user_with_posts(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    user = crud.get_user_posts(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users/create", response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@app.put("/users/update/{user_id}", response_model=schemas.User)
def update_user(user: schemas.UserCreate, user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, user, user_id)


@app.delete("/users/delete/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id)


@app.get("/posts", response_model=list[schemas.PostWithUserId])
def get_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)


@app.get("/posts/{post_id}", response_model=schemas.PostWithUserId)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.post("/posts/create", response_model=schemas.PostWithUserId, status_code=201)
def create_user_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_user_post(db, post)


@app.put("/posts/update/{post_id}", response_model=schemas.PostWithUserId)
def update_user_post(post: schemas.PostBase, post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.update_post(db, post, post_id)


@app.delete("/posts/delete/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    crud.delete_post(db, post_id)
