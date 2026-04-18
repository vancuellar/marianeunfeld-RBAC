from sqlalchemy import Column, Integer, String, Enum
from app.db.database import Base
import enum


class Role(str, enum.Enum):
    admin = "admin"
    client = "client"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(Enum(Role), default=Role.client, nullable=False)
