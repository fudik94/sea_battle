# Sea Battle CLI 🚢
*(academic project — PPTIT)*

A terminal-based Sea Battle game written in Python with a colorful CLI interface. Play solo against an AI or challenge a friend in two-player mode.

## Team

Semen Boldyrev, Fuad Ismayibayli, Ivan Aleksieiev, Danylo Chernov, Angela Cherny.

## Project Board

Trello: https://trello.com/b/aEiGl1i9

## Features

- Colorful terminal UI powered by `rich`
- Single-player mode vs AI opponent
- Two-player mode on the same machine
- Configurable board size: 5×5, 10×10, 15×15
- Ships scale to board size automatically
- Ship placement with column highlight preview
- Horizontal and vertical ship orientation
- Side-by-side board display during battle
- Battle log — last 5 actions with color coding
- Save and load custom ship sets
- Ship overlap and bounds validation

## How to Run

```bash
pip install rich
python main.py
```

## How to Play

1. Choose game mode: Single Player or Two Players
2. Choose board size
3. Enter your name
4. Place your ships — enter column, row, and orientation (h/v)
5. Take turns attacking — enter column and row to fire
6. Sink all enemy ships to win

## Project Structure

```
sea_battle/
├── main.py                  # Entry point
├── game_services.py         # ManagerBus — loads all services
├── main_game.py             # Game workflow
├── main_menu.py             # Menu workflow
├── main_battle.py           # Battle workflow
├── game_grid.py             # Game grid (configurable size)
├── game_interface.py        # CLI output and input (rich)
├── grid_object_enum.py      # Tile types (empty, ship, hit, miss)
├── grid_part.py             # Ship shape on grid
├── ship.py                  # Ship class
├── ship_representor.py      # Ship + battle state
├── ship_collection.py       # Ship tracking and limits
├── ship_constructor.py      # Ship builder
├── ship_saver.py            # Save/load ship sets (JSON)
├── controller_class.py      # Base controller
├── player_controller.py     # Player input controller
└── computer_controller.py   # AI controller
```

## Requirements

- Python 3.10+
- rich 15.0+
