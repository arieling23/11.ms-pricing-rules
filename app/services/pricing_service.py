from app.repositories.pricing_repo import PricingRepository

class PricingService:
    def __init__(self, session):
        self.session = session

    async def list_rules(self):
        return await PricingRepository.get_all(self.session)

    async def add_rule(self, rule_name, base_price, multiplier):
        return await PricingRepository.create(self.session, rule_name, base_price, multiplier)
