from controller_class import ControllerClass
from game_interface import GameInterface


class PlayerController(ControllerClass):
    def __init__(self, name="Player"):
        super().__init__(name)
        self.ui = GameInterface()

    def take_turn(self, grid) -> tuple[int, int]:
        self.ui.console.print(f"\n[bold cyan]Commander {self.name}! We await your orders. Pick a target![/bold cyan]")
        while True:
            x_raw = self.ui.ask_input(f"  x→ column (0-{grid.size - 1}): ")
            y_raw = self.ui.ask_input(f"  y↓ row    (0-{grid.size - 1}): ")
            if x_raw.isdigit() and y_raw.isdigit():
                x, y = int(x_raw), int(y_raw)
                if grid.is_within_bounds(x, y):
                    self.ui.console.print(f"[dim]Firing at ({x}, {y})...[/dim]")
                    return x, y
            self.ui.console.print(f"[yellow][HINT] Numbers must be between 0 and {grid.size - 1}[/yellow]")

    def place_ships(self, grid, ships: list):
        self.ui.console.print(f"\n[bold cyan]Captain {self.name}! We have {len(ships)} ship(s) to position. Let's move![/bold cyan]\n")
        input("  Press Enter to begin placement...")
        for i, ship in enumerate(ships):
            while True:
                self.ui.preset_placement_screen(grid, self.name, ship.name, ship.size)
                self.ui.console.print(f"[dim]Ship {i + 1} of {len(ships)}[/dim]")
                x_raw = self.ui.ask_input(f"  x→ column (0-{grid.size - 1}): ")
                if not x_raw.isdigit() or not grid.is_within_bounds(int(x_raw), 0):
                    self.ui.console.print(f"[yellow][HINT] Enter a number between 0 and {grid.size - 1}[/yellow]")
                    continue
                x = int(x_raw)
                self.ui.preset_placement_screen(grid, self.name, ship.name, ship.size, highlight_col=x)
                self.ui.console.print(f"[dim]Ship {i + 1} of {len(ships)}[/dim]")
                y_raw = self.ui.ask_input(f"  y↓ row    (0-{grid.size - 1}): ")
                if not y_raw.isdigit() or not grid.is_within_bounds(0, int(y_raw)):
                    self.ui.console.print(f"[yellow][HINT] Enter a number between 0 and {grid.size - 1}[/yellow]")
                    continue
                y = int(y_raw)
                if ship.size == 1:
                    orientation = 'h'
                else:
                    o_raw = self.ui.ask_input("  Orientation (h/v): ").lower()
                    orientation = o_raw if o_raw in ('h', 'v') else 'h'
                if orientation == 'v':
                    ship.grid_part.cells = [(0, i) for i in range(ship.size)]
                else:
                    ship.grid_part.cells = [(i, 0) for i in range(ship.size)]
                if ship.grid_part.place(grid, x, y):
                    self.ui.console.print(f"[bold green]{ship.name} is in position, Captain![/bold green]")
                    break
                self.ui.console.print("[yellow][HINT] Can't place there — out of bounds or overlaps[/yellow]")
        self.ui.console.print(f"\n[bold green]All ships are positioned, Captain {self.name}! Ready for battle![/bold green]\n")
        input("  Press Enter to continue...")
