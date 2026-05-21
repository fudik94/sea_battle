import random
from controller_class import ControllerClass
from grid_object_enum import GridObject

class ComputerController(ControllerClass):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __init__(self, name="Computer", difficulty=MEDIUM):
        super().__init__(name)
        self.difficulty = difficulty
        self._tried: set[tuple[int, int]] = set()

    def take_turn(self, grid) -> tuple[int, int]:
        available = [
            (x, y)
            for x in range(grid.size)
            for y in range(grid.size)
            if (x, y) not in self._tried
        ]
        x, y = random.choice(available)
        self._tried.add((x, y))
        return x, y

    def place_ships(self, grid, ships: list):
        for ship in ships:
            placed = False
            while not placed:
                x = random.randint(0, grid.size - 1)
                y = random.randint(0, grid.size - 1)
                horizontal = random.choice([True, False])
                cells = [(x + i, y) if horizontal else (x, y + i) for i in range(ship.size)]
                ship.grid_part.cells = cells
                placed = ship.grid_part.place(grid, 0, 0)
