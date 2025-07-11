from app.models.pricing_rule import PricingRule
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class PricingRepository:
    @staticmethod
    async def get_all(session: AsyncSession):
        result = await session.execute(select(PricingRule))
        return result.scalars().all()

    @staticmethod
    async def create(session: AsyncSession, rule_name, base_price, multiplier):
        rule = PricingRule(rule_name=rule_name, base_price=base_price, multiplier=multiplier)
        session.add(rule)
        await session.commit()
        await session.refresh(rule)
        return rule
