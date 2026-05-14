class GameGrid:
    def __init__(self, size=10):
        self.size = size
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def get_cell(self, x, y):
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        self.grid[y][x] = value

    def is_within_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def reset(self):
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
