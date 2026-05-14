# Sea Battle CLI 🚢
*(academic project — PPTIT)*
 
A terminal-based Sea Battle game written in Python. Two players compete to destroy each other's fleet. Features a custom ship builder and an AI opponent for solo play.

## Team
 
Semen Boldyrev, Fuad Ismayibayli, Ivan Aleksieiev, Danylo Chernov, Angela Cherny.

## Project Board
 
Trello: https://trello.com/b/aEiGl1i9

## Features
 
- 10×10 game board with CLI rendering
- Custom ship builder — design and save your own fleet
- Single-player mode with AI opponent
- Modular architecture for easy extension
- Ship placement validation
- Progress tracking across sessions
## Project Structure
 
```
sea-battle-cli/
├── main.py              # Entry point
├── GameServices.py      # ManagerBus — loads all services
├── MainGame.py          # Game workflow
├── MainMenu.py          # Menu workflow
├── MainBattle.py        # Battle workflow
├── GameGrid.py          # 10×10 game grid
├── GameInterface.py     # CLI output and input
├── Ship.py              # Ship class
├── ShipCollection.py    # Ship tracking
├── ShipConstructor.py   # Custom ship builder
├── PlayerController.py  # Player input controller
└── ComputerController.py# AI controller
```
 
## Requirements
 
- Python 3.10+
