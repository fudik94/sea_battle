from grid_object_enum import GridObject

class GameGrid:
    DEFAULT_SIZE = 5

    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.grid = [[GridObject.EMPTY for _ in range(self.size)] for _ in range(self.size)]

    def get_cell(self, x, y):
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        self.grid[y][x] = value

    def is_within_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def can_fit_ship(self, grid_part):
        max_x = max(dx for dx, dy in grid_part.cells)
        max_y = max(dy for dx, dy in grid_part.cells)
        return max_x < self.size and max_y < self.size

    def reset(self):
        self.grid = [[GridObject.EMPTY for _ in range(self.size)] for _ in range(self.size)]
