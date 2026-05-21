from controller_class import ControllerClass
from game_interface import GameInterface

class PlayerController(ControllerClass):
    def __init__(self, name="Player"):
        super().__init__(name)
        self.ui = GameInterface()

    def take_turn(self, grid) -> tuple[int, int]:
        while True:
            self.ui.show_text(f"{self.name}, enter attack coordinates (x y):")
            self.ui.show_all()
            raw = self.ui.ask_input("> ").split()
            if len(raw) == 2 and all(r.isdigit() for r in raw):
                x, y = int(raw[0]), int(raw[1])
                if grid.is_within_bounds(x, y):
                    return x, y
            self.ui.show_hint(f"Enter two numbers between 0 and {grid.size - 1}")
            self.ui.show_all()

    def place_ships(self, grid, ships: list):
        for ship in ships:
            while True:
                self.ui.show_text(f"{self.name}, place '{ship.name}' (size {ship.size}). Enter x y:")
                self.ui.show_all()
                raw = self.ui.ask_input("> ").split()
                if len(raw) == 2 and all(r.isdigit() for r in raw):
                    x, y = int(raw[0]), int(raw[1])
                    if ship.grid_part.place(grid, x, y):
                        self.ui.show_text(f"Ship placed!")
                        self.ui.show_all()
                        break
                self.ui.show_hint("Invalid position, try again")
                self.ui.show_all()
