from sqlalchemy import Column, Float, Integer, String

from core.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    tax = Column(Float, nullable=True)
