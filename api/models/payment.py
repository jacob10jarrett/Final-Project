# models/payment.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    card_number = Column(String(16), nullable=False)  # Example: 1234 5678 9012 3456
    payment_type = Column(String(50), nullable=False)  # Example: 'Credit', 'Debit', 'PayPal'
    transaction_status = Column(String(50), nullable=False)  # Example: 'Success', 'Failed', 'Pending'

    order = relationship("Order", back_populates="payments")
