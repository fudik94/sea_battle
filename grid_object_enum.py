from enum import Enum

class GridObject(Enum):
    EMPTY = '.'
    SHIP = 'X'
    HIT = '*'
    MISS = 'O'
