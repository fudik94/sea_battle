from main_game import MainGame

class GameServices:
    def __init__(self):
        self.game = MainGame()

    def launch(self):
        self.game.start()
