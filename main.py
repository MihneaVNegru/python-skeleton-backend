from fastapi import FastAPI
from api.health import router as health_router
from api.items import router as items_router
from api.auth import router as auth_router
from core.database import engine, Base

app=FastAPI(title="Be Skeleton Python", version="1.0.0")

app.include_router(health_router, prefix="/api")
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(items_router, prefix="/api/items")

@app.get("/")
def read_root():
    return {"message": "Welcome to the central hub! Go to /api/health for health check"}


