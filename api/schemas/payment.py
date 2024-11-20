from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    order_id: int
    card_number: str
    payment_type: str
    transaction_status: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    card_number: Optional[str] = None
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None

class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True
