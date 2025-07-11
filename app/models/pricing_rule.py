from sqlalchemy import Column, Integer, String, Float
from app.db.db import Base

class PricingRule(Base):
    __tablename__ = "pricing_rules"

    id = Column(Integer, primary_key=True, index=True)
    rule_name = Column(String, nullable=False)
    base_price = Column(Float, nullable=False)
    multiplier = Column(Float, nullable=False)
