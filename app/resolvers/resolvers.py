import strawberry
from typing import List
import sys

# ✅ Soporte para versiones < 3.10
if sys.version_info >= (3, 10):
    from builtins import anext
else:
    async def anext(aiter):
        return await aiter.__anext__()

from app.services.pricing_service import PricingService
from app.db.db import get_session

@strawberry.type
class PricingRuleType:
    id: int
    rule_name: str
    base_price: float
    multiplier: float

@strawberry.type
class Query:
    @strawberry.field
    async def pricing_rules(self, info) -> List[PricingRuleType]:
        session_gen = get_session()
        service = PricingService(await anext(session_gen))
        return await service.list_rules()

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_pricing_rule(self, info, rule_name: str, base_price: float, multiplier: float) -> PricingRuleType:
        session_gen = get_session()
        service = PricingService(await anext(session_gen))
        return await service.add_rule(rule_name, base_price, multiplier)
