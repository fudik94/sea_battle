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
        size = menu.choose_board_size()
        self.player_board = GameGrid(size)
        self.enemy_board = GameGrid(size)

    def _make_ships(self):
        return [
            ShipConstructor.create("Destroyer", 2),
            ShipConstructor.create("Submarine", 3),
            ShipConstructor.create("Battleship", 4),
        ]

    def _make_collection(self, ships):
        collection = ShipCollection()
        for ship in ships:
            collection.add(ShipRepresentor(ship))
        return collection

    def battle(self):
        player_ships_list = self._make_ships()
        enemy_ships_list = self._make_ships()

        if self.mode == MainMenu.TWO_PLAYERS:
            player1 = PlayerController("Player 1")
            player2 = PlayerController("Player 2")
        else:
            player1 = PlayerController("Player")
            player2 = ComputerController()

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
