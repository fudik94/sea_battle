from ship_representor import ShipRepresentor

class ShipCollection:
    def __init__(self):
        self.ships: list[ShipRepresentor] = []

    def add(self, ship_representor: ShipRepresentor):
        self.ships.append(ship_representor)

    def all_sunk(self):
        return all(s.is_sunk() for s in self.ships)

    def get_active(self):
        return [s for s in self.ships if not s.is_sunk()]

    def count(self):
        return len(self.ships)
