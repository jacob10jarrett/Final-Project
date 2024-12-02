from sqlalchemy import Column, Integer, String, Float, DateTime, DECIMAL
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount = Column(DECIMAL(5, 2), nullable=False)
    expiration_date = Column(DateTime, nullable=False)