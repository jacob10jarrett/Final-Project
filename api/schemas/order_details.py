from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class OrderDetailBase(BaseModel):
    quantity: int
    price: float


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    menu_item_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    quantity: Optional[int] = None
    price: Optional[float] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    menu_item: Sandwich = None

    class Config:
        from_attributes = True
