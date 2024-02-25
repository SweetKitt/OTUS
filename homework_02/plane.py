from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel=0, fuel_consumption=1, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_plus):
        if cargo_plus + self.cargo <= self.max_cargo:
            self.cargo += cargo_plus
        else:
            raise CargoOverload('Cargo Over load')

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
