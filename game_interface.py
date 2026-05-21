class GameInterface:
    def __init__(self):
        self._buffer: list[tuple[int, str]] = []

    def show(self, data):
        pass

    def ask(self, prompt: str) -> str:
        return ""

    def ask_input(self, prompt: str) -> str:
        return input(prompt).strip()

    def show_grid(self, grid, priority: int = 0):
        for row in grid.grid:
            self._buffer.append((priority, ' '.join(cell.value for cell in row)))

    def show_list(self, items: list, priority: int = 0):
        for i, item in enumerate(items):
            self._buffer.append((priority, f"{i + 1}. {item}"))

    def show_text(self, text: str, priority: int = 0):
        self._buffer.append((priority, text))

    def show_hint(self, hint: str, priority: int = 0):
        self._buffer.append((priority, f"[HINT] {hint}"))

    def show_list_return_answer(self, items: list):
        self.show_all()
        self.show_list(items)
        self.show_all()
        while True:
            raw = input("Enter number: ").strip()
            if raw.isdigit():
                index = int(raw) - 1
                if 0 <= index < len(items):
                    return items[index]
            print(f"Please enter a number between 1 and {len(items)}")

    def show_all(self):
        for _, line in sorted(self._buffer, key=lambda x: x[0], reverse=True):
            print(line)
        self._buffer.clear()

    def preset_battle_screen(self, player_grid, enemy_grid):
        self.show_text("=== YOUR BOARD ===", priority=2)
        self.show_grid(player_grid, priority=2)
        self.show_text("=== ENEMY BOARD ===", priority=1)
        self.show_grid(enemy_grid, priority=1)

    def preset_menu_screen(self, title: str, options: list):
        self.show_text(title, priority=1)
        self.show_list(options, priority=0)
