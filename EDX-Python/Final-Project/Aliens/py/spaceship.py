class Spaceship:
    def __init__(self, coordinate_x=2, size=3) -> None:
        self.size = size
        self.ship = ["⬛"] * (size // 2) + ["🛸"] + ["⬛"] * (size // 2)
        self.coordinate_x = coordinate_x

    @property
    def coordinate_x(self):
        return self._coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, coordinate_x):
        if 0 <= coordinate_x <= self.size - 1:
            self._coordinate_x = coordinate_x
        else:
            pass

    def move(self, coordinate_x):
        index = 0
        for i, value in enumerate(self.ship):
            if value == "🛸":
                index = i
        try:
            self.ship[index] = "⬛"
            self.ship[coordinate_x] = "🛸"
        except IndexError:
            return False

    def shoot(self, coordinate_x):
        # The '1' is meant to be the damage that can be implemented in the future.
        return (coordinate_x, 1)