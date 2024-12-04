from pydantic import BaseModel, validator
from typing import Optional
from enum import Enum

class PaymentType(str, Enum):
    credit = 'Credit'
    debit = 'Debit'
    paypal = 'PayPal'

class TransactionStatus(str, Enum):
    success = 'Success'
    failed = 'Failed'
    pending = 'Pending'

class PaymentBase(BaseModel):
    order_id: int
    card_number: str
    payment_type: PaymentType
    transaction_status: TransactionStatus

    @validator('card_number')
    def validate_card_number(cls, v):
        if len(v) != 16 or not v.isdigit():
            raise ValueError("Card number must be a 16-digit number.")
        return v

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    card_number: Optional[str] = None
    payment_type: Optional[PaymentType] = None
    transaction_status: Optional[TransactionStatus] = None

    @validator('card_number')
    def validate_card_number(cls, v):
        if v is not None and (len(v) != 16 or not v.isdigit()):
            raise ValueError("Card number must be a 16-digit number.")
        return v

class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True
    1