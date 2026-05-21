from grid_object_enum import GridObject

class GridPart:
    def __init__(self, cells: list[tuple[int, int]]):
        self.cells = cells

    def has_overlap(self, grid, origin_x, origin_y):
        for dx, dy in self.cells:
            x, y = origin_x + dx, origin_y + dy
            if grid.is_within_bounds(x, y) and grid.get_cell(x, y) != GridObject.EMPTY:
                return True
        return False

    def fits(self, grid, origin_x, origin_y):
        if not grid.can_fit_ship(self):
            return False
        for dx, dy in self.cells:
            x, y = origin_x + dx, origin_y + dy
            if not grid.is_within_bounds(x, y):
                return False
        if self.has_overlap(grid, origin_x, origin_y):
            return False
        return True

    def place(self, grid, origin_x, origin_y):
        if not self.fits(grid, origin_x, origin_y):
            return False
        for dx, dy in self.cells:
            grid.set_cell(origin_x + dx, origin_y + dy, GridObject.SHIP)
        return True
