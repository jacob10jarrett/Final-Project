from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .menu_items import MenuItem


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
    menu_item: Optional[MenuItem] = None
    quantity: int
    price: float

    class Config:
        from_attributes = True
