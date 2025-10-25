from fastapi import FastAPI
from app.api import flights, users
from app.core.config import settings

app = FastAPI(title=settings.app_name, version=settings.version)

app.include_router(flights.router, prefix="/flights")
app.include_router(users.router, prefix="/users")

@app.get("/", summary="Healthcheck")
def root():
    return {"status": "ok", "service": settings.app_name, "version": settings.version}
