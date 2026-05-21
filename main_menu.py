from game_grid import GameGrid
from game_interface import GameInterface

class MainMenu:
    SINGLE_PLAYER = "Single Player (vs Computer)"
    TWO_PLAYERS = "Two Players"
    EXIT = "Exit"

    def __init__(self):
        self.ui = GameInterface()

    def show(self) -> str:
        self.ui.show_text("=== SEA BATTLE ===")
        self.ui.show_all()
        return self.show_options()

    def show_options(self) -> str:
        options = [self.SINGLE_PLAYER, self.TWO_PLAYERS, self.EXIT]
        return self.ui.show_list_return_answer(options)

    def choose_board_size(self) -> int:
        self.ui.show_text("Choose board size:")
        self.ui.show_all()
        sizes = [str(s) for s in GameGrid.PRESET_SIZES]
        choice = self.ui.show_list_return_answer(sizes)
        return int(choice)
