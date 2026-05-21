from grid_object_enum import GridObject
from game_interface import GameInterface

class MainBattle:
    def __init__(self, player_board, enemy_board, player_controller, enemy_controller,
                 player_ships, enemy_ships):
        self.player_board = player_board
        self.enemy_board = enemy_board
        self.player_controller = player_controller
        self.enemy_controller = enemy_controller
        self.player_ships = player_ships
        self.enemy_ships = enemy_ships
        self.ui = GameInterface()

    def start(self):
        while True:
            self._show_boards()

            x, y = self.player_controller.take_turn(self.enemy_board)
            self._apply_shot(self.enemy_board, self.enemy_ships, x, y, "Enemy")
            if self.enemy_ships.all_sunk():
                self.ui.show_text("You win!")
                self.ui.show_all()
                break

            x, y = self.enemy_controller.take_turn(self.player_board)
            self.ui.show_text(f"{self.enemy_controller.name} attacks ({x}, {y})")
            self._apply_shot(self.player_board, self.player_ships, x, y, "Your")
            if self.player_ships.all_sunk():
                self.ui.show_text("Computer wins!")
                self.ui.show_all()
                break

    def _apply_shot(self, board, ships, x, y, label: str):
        cell = board.get_cell(x, y)
        if cell == GridObject.SHIP:
            board.set_cell(x, y, GridObject.HIT)
            for ship in ships.ships:
                ship.hit()
            self.ui.show_text(f"Hit on {label} board at ({x}, {y})!")
        else:
            board.set_cell(x, y, GridObject.MISS)
            self.ui.show_text(f"Miss on {label} board at ({x}, {y})")
        self.ui.show_all()

    def _show_boards(self):
        self.ui.preset_battle_screen(self.player_board, self.enemy_board)
        self.ui.show_all()

    def check_winner(self):
        if self.enemy_ships.all_sunk():
            return self.player_controller.name
        if self.player_ships.all_sunk():
            return self.enemy_controller.name
        return None
