from board import Board

class MainGame:
    def __init__(self):
        self.player_board = Board()
        self.enemy_board = Board()

    def start(self):
        self.setup()
        self.battle()
        self.end()

    def setup(self):
        pass

    def battle(self):
        pass

    def end(self):
        pass
