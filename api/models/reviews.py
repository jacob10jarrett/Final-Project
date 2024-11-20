from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base
from sqlalchemy.orm import relationship
from .customers import Customer
from .menu_items import MenuItem

class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey(Customer.id), nullable=False)
    menu_item_id = Column(Integer, ForeignKey(MenuItem.menuItemID), nullable=False)
    score = Column(Integer, nullable=False)  # Assuming a rating system (e.g., 1-5)
    review_text = Column(String(500), nullable=True)  # Optional text review

    # Relationships
    customer = relationship("Customer", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")