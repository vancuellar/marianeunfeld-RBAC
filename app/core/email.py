from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.core.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_USERNAME,
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)


async def send_booking_notification(booking) -> None:
    body = f"""
    <h2>Nuevo agendamiento recibido</h2>
    <table>
        <tr><td><b>Nombre:</b></td><td>{booking.first_name} {booking.last_name}</td></tr>
        <tr><td><b>Email:</b></td><td>{booking.email}</td></tr>
        <tr><td><b>Teléfono:</b></td><td>{booking.phone or "—"}</td></tr>
        <tr><td><b>Servicio:</b></td><td>{booking.service or "—"}</td></tr>
        <tr><td><b>Fecha del evento:</b></td><td>{booking.event_date or "—"}</td></tr>
        <tr><td><b>Local:</b></td><td>{booking.event_location or "—"}</td></tr>
        <tr><td><b>Mensaje:</b></td><td>{booking.message or "—"}</td></tr>
    </table>
    """

    message = MessageSchema(
        subject="✨ Nueva solicitud de agendamiento — Maria Neunfeld",
        recipients=[settings.NOTIFY_EMAIL],
        body=body,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    await fm.send_message(message)
