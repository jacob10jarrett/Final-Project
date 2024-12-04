from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    card_number = Column(String(16), nullable=False)
    payment_type = Column(String(50), nullable=False)
    transaction_status = Column(String(50), nullable=False)

    # Relationship
    order = relationship("Order", back_populates="payments")
