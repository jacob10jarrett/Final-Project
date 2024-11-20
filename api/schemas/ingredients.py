from pydantic import BaseModel
from typing import Optional


class IngredientBase(BaseModel):
    Name: str
    Unit: str
    Amount: int


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    Name: Optional[str] = None
    Unit: Optional[str] = None
    Amount: Optional[int] = None


class Ingredient(IngredientBase):
    IngredientID: int

    class ConfigDict:
        from_attributes = True
