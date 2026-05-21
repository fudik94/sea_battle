from ship_representor import ShipRepresentor

class ShipCollection:
    MAX_SHIPS = 5

    def __init__(self, max_ships: int = MAX_SHIPS):
        self.ships: list[ShipRepresentor] = []
        self.max_ships = max_ships

    def add(self, ship_representor: ShipRepresentor):
        if len(self.ships) >= self.max_ships:
            return False
        self.ships.append(ship_representor)
        return True

    def all_sunk(self):
        return all(s.is_sunk() for s in self.ships)

    def get_active(self):
        return [s for s in self.ships if not s.is_sunk()]

    def count(self):
        return len(self.ships)
