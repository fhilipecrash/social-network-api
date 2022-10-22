from api import database
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import schemas, crud


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
