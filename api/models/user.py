from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    name = Column(String)
    password = Column(String)

    posts = relationship("Post", back_populates="user")
