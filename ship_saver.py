import json
from ship import Ship
from ship_constructor import ShipConstructor

class ShipSaver:
    @staticmethod
    def save(ships: list[Ship], filepath: str):
        data = [
            {"name": ship.name, "cells": ship.grid_part.cells}
            for ship in ships
        ]
        with open(filepath, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load(filepath: str) -> list[Ship]:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return [
            ShipConstructor.create_custom(entry["name"], [tuple(c) for c in entry["cells"]])
            for entry in data
        ]
