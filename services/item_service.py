from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemCreate
from typing import List

def create_item(db: Session, item_data: ItemCreate) -> Item:
    # Create the database model instance
    db_item = Item(
        name=item_data.name,
        description=item_data.description,
        price=item_data.price,
        tax=item_data.tax
    )
    # Add to session and commit
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_items(db: Session) -> List[Item]:
    return db.query(Item).all()

def get_item_by_id(db: Session, item_id: int) -> Item:
    return db.query(Item).filter(Item.id == item_id).first()