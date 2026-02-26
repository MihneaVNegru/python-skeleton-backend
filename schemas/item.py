
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
class ItemResponse(ItemCreate):
    id: int
 