from controller_class import ControllerClass

class ComputerController(ControllerClass):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __init__(self, name="Computer", difficulty=MEDIUM):
        super().__init__(name)
        self.difficulty = difficulty

    def take_turn(self, grid):
        pass

    def place_ships(self, grid):
        pass
