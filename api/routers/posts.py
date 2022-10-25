from api.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import schemas, controllers

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.PostWithUserId])
def get_posts(db: Session = Depends(get_db)):
    return controllers.get_posts(db)


@router.get("/{post_id}", response_model=schemas.PostWithUserId)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = controllers.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.post("", response_model=schemas.PostWithUserId, status_code=201)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return controllers.create_user_post(db, post)


@router.put("/{post_id}", response_model=schemas.PostWithUserId)
def update_post(post: schemas.PostBase, post_id: int, db: Session = Depends(get_db)):
    db_post = controllers.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return controllers.update_post(db, post, post_id)


@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = controllers.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    controllers.delete_post(db, post_id)
