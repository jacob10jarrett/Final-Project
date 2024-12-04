from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    menuItemID = Column(Integer, primary_key=True, autoincrement=True)
    dishes = Column(String(100), nullable=False)  # Name of menu item (e.g., "Veggie Burger")
    category = Column(String(50), nullable=False)  # Category (e.g., "Appetizer", "Main Course")
    calories = Column(Integer, nullable=False, default=0)  # Calories in the menu item
    price = Column(Float, nullable=False)  # Price of the menu item

    # Relationships
    ingredients = relationship("MenuItemIngredient", back_populates="menu_item")  # Many-to-Many with Ingredients
    order_details = relationship("OrderDetail", back_populates="menu_item")  # One-to-Many with OrderDetails
    reviews = relationship("Review", back_populates="menu_item")
    recipes = relationship("Recipe", back_populates="menu_item")

class MenuItemIngredient(Base):
    __tablename__ = "menu_item_ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.menuItemID"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.IngredientID"), nullable=False)
    quantity = Column(Float, nullable=False)  # Quantity of ingredient needed

    # Relationships
    menu_item = relationship("MenuItem", back_populates="ingredients")  # Link to MenuItem
    ingredient = relationship("Ingredient", back_populates="menu_items")  # Link to Ingredient

from .recipes import Recipe