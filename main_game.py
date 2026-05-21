from game_grid import GameGrid
from game_interface import GameInterface
from main_battle import MainBattle
from main_menu import MainMenu
from player_controller import PlayerController
from computer_controller import ComputerController
from ship_constructor import ShipConstructor
from ship_representor import ShipRepresentor
from ship_collection import ShipCollection


class MainGame:
    def __init__(self):
        self.player_board = GameGrid()
        self.enemy_board = GameGrid()
        self.mode = None
        self.ui = GameInterface()

    def start(self):
        self.setup()
        if self.mode == MainMenu.EXIT:
            return
        self.battle()
        self.end()

    def setup(self):
        menu = MainMenu()
        self.mode = menu.show()
        if self.mode == MainMenu.EXIT:
            return
        size = menu.choose_board_size()
        self.player_board = GameGrid(size)
        self.enemy_board = GameGrid(size)

    def _make_ships(self, size: int):
        if size <= 5:
            return [
                ShipConstructor.create("Boat", 1),
                ShipConstructor.create("Destroyer", 2),
            ]
        elif size <= 10:
            return [
                ShipConstructor.create("Destroyer", 2),
                ShipConstructor.create("Submarine", 3),
                ShipConstructor.create("Battleship", 4),
            ]
        else:
            return [
                ShipConstructor.create("Destroyer", 2),
                ShipConstructor.create("Submarine", 3),
                ShipConstructor.create("Cruiser", 4),
                ShipConstructor.create("Battleship", 5),
            ]

    def _make_collection(self, ships):
        collection = ShipCollection()
        for ship in ships:
            collection.add(ShipRepresentor(ship))
        return collection

    def _ask_name(self, prompt: str) -> str:
        self.ui.console.print(f"\n[bold cyan]{prompt}[/bold cyan]")
        name = self.ui.ask_input("  > ").strip()
        return name if name else "Captain"

    def battle(self):
        size = self.player_board.size
        player_ships_list = self._make_ships(size)
        enemy_ships_list = self._make_ships(size)

        if self.mode == MainMenu.TWO_PLAYERS:
            name1 = self._ask_name("Player 1, what shall we call you, Captain?")
            name2 = self._ask_name("Player 2, what shall we call you, Captain?")
            player1 = PlayerController(name1)
            player2 = PlayerController(name2)
        else:
            name1 = self._ask_name("Captain, what shall we call you?")
            player1 = PlayerController(name1)
            player2 = ComputerController("Enemy AI")

        player1.place_ships(self.player_board, player_ships_list)
        player2.place_ships(self.enemy_board, enemy_ships_list)

        player_collection = self._make_collection(player_ships_list)
        enemy_collection = self._make_collection(enemy_ships_list)

        battle = MainBattle(
            self.player_board, self.enemy_board,
            player1, player2,
            player_collection, enemy_collection
        )
        battle.start()

    def end(self):
        self.ui.show_text("Thanks for playing!")
        self.ui.show_all()
