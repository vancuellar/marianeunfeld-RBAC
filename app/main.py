from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import auth, users, bookings
from app.db.database import Base, engine
import app.models.user  # noqa: F401
import app.models.booking  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Maria Neunfeld RBAC API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(bookings.router, prefix="/bookings", tags=["bookings"])


@app.get("/health")
def health():
    return {"status": "ok"}
