from game_grid import GameGrid

class MainMenu:
    def __init__(self):
        pass

    def show(self):
        self.show_options()

    def show_options(self):
        pass

    def handle_input(self):
        pass

    def choose_board_size(self) -> int:
        return GameGrid.DEFAULT_SIZE
