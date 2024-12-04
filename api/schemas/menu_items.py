from pydantic import BaseModel
from typing import Optional, List


class MenuItemBase(BaseModel):
    dishes: str
    category: str
    calories: int
    price: float


class MenuItemCreate(MenuItemBase):
    ingredients: List[int]


class MenuItemUpdate(BaseModel):
    dishes: Optional[str] = None
    category: Optional[str] = None
    calories: Optional[int] = None
    price: Optional[float] = None
    ingredients: Optional[List[int]] = None


class MenuItemIngredient(BaseModel):
    ingredient_id: int
    quantity: float


class MenuItem(MenuItemBase):
    menuItemID: int
    ingredients: List[MenuItemIngredient] = []

    class Config:
        orm_mode = True
