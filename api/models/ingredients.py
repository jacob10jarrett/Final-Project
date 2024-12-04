from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    IngredientID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), unique=True, nullable=False)  # Ingredient name
    Unit = Column(String(50), nullable=False)  # Unit of measurement
    Amount = Column(Integer, nullable=False, default=0)  # Quantity available

    # Relationships
    menu_items = relationship("MenuItemIngredient", back_populates="ingredient")

# Late import to resolve circular dependency
from .menu_items import MenuItemIngredient
