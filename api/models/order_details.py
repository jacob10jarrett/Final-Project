from sqlalchemy import Column, ForeignKey, Integer, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)
    quantity = Column(Integer, index=True, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    menu_item = relationship("Sandwich", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")