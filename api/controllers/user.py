from sqlalchemy.orm import Session
from api import schemas, models


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    return db_user


def get_user_with_posts(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    return db_user


def get_user_posts(db: Session, user_id: int):
    return db.query(models.Post).filter(models.Post.user_id == user_id).all()


def get_user_by_email(db: Session, email: str):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        return None
    return db_user


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, name=user.name,
                          password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserCreate, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    db_user.name = user.name
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
