from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional
from app.models.booking import BookingStatus


class BookingCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    service: Optional[str] = None
    event_date: Optional[date] = None
    event_location: Optional[str] = None
    message: Optional[str] = None


class BookingStatusUpdate(BaseModel):
    status: BookingStatus


class BookingOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    service: Optional[str]
    event_date: Optional[date]
    event_location: Optional[str]
    message: Optional[str]
    status: BookingStatus
    created_at: datetime

    model_config = {"from_attributes": True}
