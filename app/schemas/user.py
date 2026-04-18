from pydantic import BaseModel, EmailStr
from app.models.user import Role


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None
    role: Role = Role.client


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None
    role: Role

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
