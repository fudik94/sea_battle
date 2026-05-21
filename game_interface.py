class GameInterface:
    def __init__(self):
        self._buffer: list[str] = []

    def show(self, data):
        pass

    def ask(self, prompt: str) -> str:
        return ""

    def ask_input(self, prompt: str) -> str:
        return input(prompt).strip()

    def show_grid(self, grid):
        for row in grid.grid:
            self._buffer.append(' '.join(cell.value for cell in row))

    def show_list(self, items: list):
        for i, item in enumerate(items):
            self._buffer.append(f"{i + 1}. {item}")

    def show_text(self, text: str):
        self._buffer.append(text)

    def show_hint(self, hint: str):
        self._buffer.append(f"[HINT] {hint}")

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
        for line in self._buffer:
            print(line)
        self._buffer.clear()
