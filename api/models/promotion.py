from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..dependencies.database import Base

class PromotionBase(BaseModel):
    code: str
    discount: float
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount: Optional[float] = None
    expiration_date: Optional[datetime] = None

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True
