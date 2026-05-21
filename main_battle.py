from collections import deque
from grid_object_enum import GridObject
from game_interface import GameInterface


class MainBattle:
    LOG_SIZE = 5

    def __init__(self, player_board, enemy_board, player_controller, enemy_controller,
                 player_ships, enemy_ships):
        self.player_board = player_board
        self.enemy_board = enemy_board
        self.player_controller = player_controller
        self.enemy_controller = enemy_controller
        self.player_ships = player_ships
        self.enemy_ships = enemy_ships
        self.ui = GameInterface()
        self.log: deque[str] = deque(maxlen=self.LOG_SIZE)

    def _add_log(self, msg: str):
        self.log.append(msg)

    def start(self):
        while True:
            self._show_boards()

            x, y = self.player_controller.take_turn(self.enemy_board)
            msg = self._apply_shot(self.enemy_board, self.enemy_ships, x, y, "Enemy")
            self._add_log(f"[yellow]► {msg}[/yellow]")
            if self.enemy_ships.all_sunk():
                self._show_boards()
                self.ui.console.print("[bold green]\n Victory! All enemy ships have been sunk, Commander! \n[/bold green]")
                break

            x, y = self.enemy_controller.take_turn(self.player_board)
            msg = self._apply_shot(self.player_board, self.player_ships, x, y, "Our")
            self._add_log(f"[red]◄ {msg}[/red]")
            if self.player_ships.all_sunk():
                self._show_boards()
                self.ui.console.print("[bold red]\n All our ships are lost, Captain. The enemy wins. \n[/bold red]")
                break

    def _apply_shot(self, board, ships, x, y, label: str) -> str:
        cell = board.get_cell(x, y)
        if cell == GridObject.SHIP:
            board.set_cell(x, y, GridObject.HIT)
            for rep in ships.ships:
                if not rep.is_sunk():
                    rep.hit()
                    if rep.is_sunk():
                        return f"DIRECT HIT at ({x},{y})! {label} ship has been sunk!"
                    break
            return f"HIT! {label} ship is taking damage at ({x},{y})!"
        else:
            board.set_cell(x, y, GridObject.MISS)
            return f"Miss... The shell splashed into the sea at ({x},{y})"

    def _show_boards(self):
        self.ui.preset_battle_screen(self.player_board, self.enemy_board, list(self.log))

    def check_winner(self):
        if self.enemy_ships.all_sunk():
            return self.player_controller.name
        if self.player_ships.all_sunk():
            return self.enemy_controller.name
        return None
