from board import Board
from main_battle import MainBattle
from main_menu import MainMenu

class MainGame:
    def __init__(self):
        self.player_board = Board()
        self.enemy_board = Board()

    def start(self):
        self.setup()
        self.battle()
        self.end()

    def setup(self):
        menu = MainMenu()
        menu.show()

    def battle(self):
        battle = MainBattle(self.player_board, self.enemy_board)
        battle.start()

    def end(self):
        pass
