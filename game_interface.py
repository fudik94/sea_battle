class GameInterface:
    def show(self, data):
        pass

    def ask(self, prompt: str) -> str:
        return ""

    def show_grid(self, grid):
        for row in grid.grid:
            print(' '.join(cell.value for cell in row))

