from game import Game

class GameServices:
    def __init__(self):
        self.game = Game()

    def launch(self):
        self.game.start()
