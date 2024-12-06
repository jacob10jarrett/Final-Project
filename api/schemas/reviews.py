from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    score: int
    review_text: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    customer_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    score: Optional[int] = None
    review_text: Optional[str] = None

class Review(ReviewBase):
    review_id: int

    class Config:
        orm_mode = True
