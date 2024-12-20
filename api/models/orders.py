from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=True)
    status = Column(String(50), nullable=True)
    tracking_number = Column(String(100), nullable=True)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationships
    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populates="order")
    customer = relationship("Customer", back_populates="orders")
