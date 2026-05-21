from grid_part import GridPart

class Ship:
    def __init__(self, name: str, cells: list[tuple[int, int]]):
        self.name = name
        self.grid_part = GridPart(cells)
        self.size = len(cells)
        self.hits = 0

    def is_sunk(self):
        return self.hits >= self.size

    def hit(self):
        self.hits += 1
