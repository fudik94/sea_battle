class GameInterface:
    def show(self, data):
        pass

    def ask(self, prompt: str) -> str:
        return ""

    def show_grid(self, grid):
        for row in grid.grid:
            print(' '.join(cell.value for cell in row))

    def show_list(self, items: list):
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")

    def show_list_return_answer(self, items: list):
        self.show_list(items)
        while True:
            raw = input("Enter number: ").strip()
            if raw.isdigit():
                index = int(raw) - 1
                if 0 <= index < len(items):
                    return items[index]
            print(f"Please enter a number between 1 and {len(items)}")

