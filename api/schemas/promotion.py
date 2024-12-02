from pydantic import BaseModel, validator
from datetime import datetime, timezone
from typing import Optional

class PromotionBase(BaseModel):
    code: str
    discount: float
    expiration_date: datetime

    @validator('discount')
    def validate_discount(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Discount must be between 0 and 100.")
        return v

    @validator('expiration_date')
    def validate_expiration_date(cls, v):
        if v < datetime.now(timezone.utc):
            raise ValueError("Expiration date cannot be in the past.")
        return v

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount: Optional[float] = None
    expiration_date: Optional[datetime] = None

    @validator('discount')
    def validate_discount(cls, v):
        if v is not None and (v < 0 or v > 100):
            raise ValueError("Discount must be between 0 and 100.")
        return v

    @validator('expiration_date')
    def validate_expiration_date(cls, v):
        if v is not None and v < datetime.now(timezone.utc):
            raise ValueError("Expiration date cannot be in the past.")
        return v

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True
