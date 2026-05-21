from ship import Ship

class ShipRepresentor:
    def __init__(self, ship: Ship):
        self.ship = ship
        self.position = None
        self.is_placed = False

    def place(self, grid, x, y):
        if self.ship.grid_part.place(grid, x, y):
            self.position = (x, y)
            self.is_placed = True
            return True
        return False

    def hit(self):
        self.ship.hit()

    def is_sunk(self):
        return self.ship.is_sunk()
