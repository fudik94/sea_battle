from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from grid_object_enum import GridObject


class GameInterface:
    SYMBOL_STYLE = {
        GridObject.EMPTY: "dim white",
        GridObject.SHIP:  "bold blue",
        GridObject.HIT:   "bold red",
        GridObject.MISS:  "yellow",
    }

    def __init__(self):
        self._buffer: list[tuple[int, str]] = []
        self.console = Console()

    def _make_grid_panel(self, grid, title: str, hidden: bool = False, highlight_col: int = None):
        table = Table(show_header=True, header_style="bold cyan", box=None, padding=(0, 1))
        table.add_column("[bold cyan]y↓ x→[/bold cyan]", style="bold cyan", no_wrap=True)
        for x in range(grid.size):
            header = f"[bold yellow on blue] {x} [/bold yellow on blue]" if x == highlight_col else str(x)
            table.add_column(header, justify="center", no_wrap=True)
        for y, row in enumerate(grid.grid):
            cells = [str(y)]
            for x_idx, cell in enumerate(row):
                display = GridObject.EMPTY if (hidden and cell == GridObject.SHIP) else cell
                style = self.SYMBOL_STYLE.get(display, "white")
                if x_idx == highlight_col:
                    cells.append(f"[{style} on blue]{display.value}[/{style} on blue]")
                else:
                    cells.append(f"[{style}]{display.value}[/{style}]")
            table.add_row(*cells)
        return Panel(table, title=f"[bold]{title}[/bold]", border_style="cyan")

    def show(self, data):
        pass

    def ask(self, prompt: str) -> str:
        return ""

    def ask_input(self, prompt: str) -> str:
        return self.console.input(f"[bold green]{prompt}[/bold green]").strip()

    def show_grid(self, grid, priority: int = 0):
        header = "  " + " ".join(str(x) for x in range(grid.size))
        self._buffer.append((priority, header))
        for y, row in enumerate(grid.grid):
            self._buffer.append((priority, str(y) + " " + " ".join(cell.value for cell in row)))

    def show_grid_hidden(self, grid, priority: int = 0):
        header = "  " + " ".join(str(x) for x in range(grid.size))
        self._buffer.append((priority, header))
        for y, row in enumerate(grid.grid):
            cells = [GridObject.EMPTY.value if c == GridObject.SHIP else c.value for c in row]
            self._buffer.append((priority, str(y) + " " + " ".join(cells)))

    def show_legend(self, priority: int = 0):
        self._buffer.append((priority, ". = empty  X = ship  * = hit  O = miss"))

    def show_list(self, items: list, priority: int = 0):
        for i, item in enumerate(items):
            self._buffer.append((priority, f"{i + 1}. {item}"))

    def show_text(self, text: str, priority: int = 0):
        self._buffer.append((priority, text))

    def show_hint(self, hint: str, priority: int = 0):
        self._buffer.append((priority, f"[yellow][HINT] {hint}[/yellow]"))

    def show_list_return_answer(self, items: list):
        self.show_list(items)
        self.show_all()
        while True:
            raw = self.console.input("[bold green]Enter number: [/bold green]").strip()
            if raw.isdigit():
                index = int(raw) - 1
                if 0 <= index < len(items):
                    return items[index]
            self.console.print(f"[yellow]Please enter a number between 1 and {len(items)}[/yellow]")

    def show_all(self):
        for _, line in sorted(self._buffer, key=lambda x: x[0], reverse=True):
            self.console.print(line)
        self._buffer.clear()

    def preset_battle_screen(self, player_grid, enemy_grid, log: list = None):
        self.console.clear()
        player_panel = self._make_grid_panel(player_grid, "YOUR BOARD")
        enemy_panel = self._make_grid_panel(enemy_grid, "ENEMY BOARD", hidden=True)
        self.console.print(Columns([player_panel, enemy_panel]))
        self.console.print("[dim]. = empty  [/dim][bold blue]X = ship[/bold blue]  [bold red]* = hit[/bold red]  [yellow]O = miss[/yellow]")
        if log:
            self.console.print("\n[bold dim]--- Battle Log ---[/bold dim]")
            for entry in log:
                self.console.print(f"  {entry}")
        used_lines = player_grid.size + 10 + (len(log) + 2 if log else 0)
        padding = max(0, self.console.size.height - used_lines)
        self.console.print("\n" * padding, end="")

    def preset_placement_screen(self, grid, player_name: str, ship_name: str, ship_size: int, highlight_col: int = None):
        self.console.clear()
        panel = self._make_grid_panel(grid, f"{player_name}: Place your ships", highlight_col=highlight_col)
        self.console.print(panel)
        self.console.print("[dim]. = empty  [/dim][bold blue]X = placed ship[/bold blue]")
        self.console.print(f"\nPlace [bold cyan]'{ship_name}'[/bold cyan] (size [bold]{ship_size}[/bold])")
        padding = max(0, self.console.size.height - grid.size - 12)
        self.console.print("\n" * padding, end="")

    def preset_menu_screen(self, title: str, options: list):
        self.show_text(title, priority=1)
        self.show_list(options, priority=0)
