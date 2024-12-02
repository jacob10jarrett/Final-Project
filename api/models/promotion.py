from sqlalchemy import Column, Integer, String, Float, DateTime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount = Column(Float, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
