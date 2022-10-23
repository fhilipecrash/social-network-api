from api.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import schemas, controllers

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.User] | schemas.User)
def get_users(email: str | None = None, db: Session = Depends(get_db)):
    if email:
        db_user = controllers.get_user_by_email(db, email)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    return controllers.get_users(db)


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = controllers.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/{user_id}/posts", response_model=list[schemas.PostWithUserId] | schemas.UserWithPosts)
def get_user_posts(user_id: int, with_user_info: bool = False, db: Session = Depends(get_db)):
    if with_user_info:
        db_user = controllers.get_user_with_posts(db, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    db_user = controllers.get_user_posts(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/create", response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = controllers.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controllers.create_user(db, user)


@router.put("/update/{user_id}", response_model=schemas.User)
def update_user(user: schemas.UserCreate, user_id: int, db: Session = Depends(get_db)):
    db_user = controllers.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return controllers.update_user(db, user, user_id)


@router.delete("/delete/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = controllers.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    controllers.delete_user(db, user_id)
