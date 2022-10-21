from sqlalchemy.orm import Session

from . import models


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.posts = db.query(models.Post).filter(
        models.Post.user_id == user_id).all()
    return user


def get_user_by_email(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    user.posts = db.query(models.Post).filter(
        models.Post.user_id == user.id).all()
    return user


def create_user(db: Session, user: models.User):
    db_user = models.User(email=user.email, name=user.name,
                          password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
