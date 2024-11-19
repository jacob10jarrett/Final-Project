from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_id: int
    total_price: Optional[float] = None
    status: Optional[str] = None
    tracking_number: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    total_price: Optional[float] = None
    status: Optional[str] = None
    tracking_number: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: List[OrderDetail] = []

    class Config:
        from_attributes = True
