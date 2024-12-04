from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)  # FK to Resource
    menu_item_id = Column(Integer, ForeignKey("menu_items.menuItemID"), nullable=False)  # FK to MenuItem
    amount = Column(Integer, nullable=False)  # Quantity needed

    # Relationships
    resource = relationship("Resource", back_populates="recipes")  # Reverse relationship to Resource
    menu_item = relationship("MenuItem", back_populates="recipes")  # Reverse relationship to MenuItem
