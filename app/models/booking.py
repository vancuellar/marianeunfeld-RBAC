from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Text, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base
import enum


class BookingStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(30))
    service = Column(String(100))
    event_date = Column(Date)
    event_location = Column(String(200))
    message = Column(Text)
    status = Column(Enum(BookingStatus), default=BookingStatus.pending, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
