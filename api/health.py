from fastapi import APIRouter

# APIRouter is exactly like 'FastAPI()', but it lets us break our API into smaller pieces.
router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend is fully operational", "layer": "api"}
