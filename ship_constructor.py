from ship import Ship

class ShipConstructor:
    @staticmethod
    def create(name: str, size: int, horizontal: bool = True) -> Ship:
        if horizontal:
            cells = [(i, 0) for i in range(size)]
        else:
            cells = [(0, i) for i in range(size)]
        return Ship(name, cells)

    @staticmethod
    def create_custom(name: str, cells: list[tuple[int, int]]) -> Ship:
        return Ship(name, cells)
