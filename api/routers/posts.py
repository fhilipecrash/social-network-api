from api.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import schemas, crud

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.PostWithUserId])
def get_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)


@router.get("/{post_id}", response_model=schemas.PostWithUserId)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.post("/create", response_model=schemas.PostWithUserId, status_code=201)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_user_post(db, post)


@router.put("/update/{post_id}", response_model=schemas.PostWithUserId)
def update_post(post: schemas.PostBase, post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.update_post(db, post, post_id)


@router.delete("/delete/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    crud.delete_post(db, post_id)
