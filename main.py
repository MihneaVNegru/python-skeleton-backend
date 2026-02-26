from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.auth import router as auth_router
from api.health import router as health_router
from api.items import router as items_router

app=FastAPI(title="Be Skeleton Python", version="1.0.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(items_router, prefix="/api/items")

@app.get("/")
def read_root():
    return {"message": "Welcome to the central hub! Go to /api/health for health check"}


