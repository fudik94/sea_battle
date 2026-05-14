from grid_object_enum import GridObject

class GridPart:
    def __init__(self, cells: list[tuple[int, int]]):
        self.cells = cells

    def fits(self, grid, origin_x, origin_y):
        for dx, dy in self.cells:
            x, y = origin_x + dx, origin_y + dy
            if not grid.is_within_bounds(x, y):
                return False
            if grid.get_cell(x, y) != GridObject.EMPTY:
                return False
        return True

    def place(self, grid, origin_x, origin_y):
        if not self.fits(grid, origin_x, origin_y):
            return False
        for dx, dy in self.cells:
            grid.set_cell(origin_x + dx, origin_y + dy, GridObject.SHIP)
        return True
