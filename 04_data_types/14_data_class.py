from dataclasses import dataclass, asdict, astuple
from decimal import Decimal


@dataclass(frozen=True)
class Cookie:
    name: str
    cost: Decimal
    quantity: int = 0

    @property
    def value_of_goods(self):
        return int(self.quantity) * self.cost


chocolate_chip = Cookie("chocolate chip", Decimal("0.75"), 13)
print(chocolate_chip.name)
print(chocolate_chip.quantity)

ginger_molasses = Cookie("ginger molasses", Decimal("1.5"), 8)
print(asdict(ginger_molasses))
print(astuple(ginger_molasses))

peanut = Cookie("Peanut Butter", Decimal("1.2"), 8)
print(peanut.value_of_goods)

c = Cookie("chocolate chip", Decimal("1.75"), 10)
# c.quantity=15 # Uncommenting this line will raise an error because the dataclass is frozen
