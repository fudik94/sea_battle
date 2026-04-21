class Board:
    def __init__(self):
        self.size = 10
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def get_cell(self, x, y):
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        self.grid[y][x] = value
