from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingOut, BookingStatusUpdate
from app.routers.users import get_current_user
from app.models.user import User, Role
from app.core.email import send_booking_notification
from app.core.config import settings

router = APIRouter()


@router.post("/", response_model=BookingOut, status_code=201)
async def create_booking(
    payload: BookingCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    booking = Booking(**payload.model_dump())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    if settings.MAIL_USERNAME and settings.NOTIFY_EMAIL:
        background_tasks.add_task(send_booking_notification, booking)
    return booking


@router.get("/", response_model=List[BookingOut])
def list_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != Role.admin:
        raise HTTPException(status_code=403, detail="Admins only")
    return db.query(Booking).order_by(Booking.created_at.desc()).all()


@router.patch("/{booking_id}", response_model=BookingOut)
def update_booking_status(
    booking_id: int,
    payload: BookingStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != Role.admin:
        raise HTTPException(status_code=403, detail="Admins only")
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    booking.status = payload.status
    db.commit()
    db.refresh(booking)
    return booking
