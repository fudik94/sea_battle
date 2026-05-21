from game_grid import GameGrid
from main_battle import MainBattle
from main_menu import MainMenu

class MainGame:
    def __init__(self):
        self.player_board = GameGrid()
        self.enemy_board = GameGrid()

    def start(self):
        self.setup()
        self.battle()
        self.end()

    def setup(self):
        menu = MainMenu()
        size = menu.choose_board_size()
        self.player_board = GameGrid(size)
        self.enemy_board = GameGrid(size)
        menu.show()

    def battle(self):
        battle = MainBattle(self.player_board, self.enemy_board)
        battle.start()

    def end(self):
        pass
