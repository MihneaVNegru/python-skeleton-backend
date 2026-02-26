
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.deps import get_current_user  # New dependency
from core.database import get_db
from models.user import User
from schemas.item import ItemCreate, ItemResponse
from services import item_service

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def create_item(
    item: ItemCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) # Now protected!
):
    return item_service.create_item(db, item)

@router.get("/", response_model=list[ItemResponse])
def get_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) # Now protected!
):
    return item_service.get_all_items(db)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) # Now protected!
):
    item = item_service.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


