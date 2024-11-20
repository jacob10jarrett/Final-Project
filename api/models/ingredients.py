from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    IngredientID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), unique=True, nullable=False)
    Unit = Column(String(50), nullable=False)  # Example: grams, liters
    Amount = Column(Integer, nullable=False, default=0)
    menu_items = relationship("MenuItemIngredient", back_populates="ingredient")
