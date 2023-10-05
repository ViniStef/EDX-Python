class Alien:
    def __init__(self, size=3) -> None:
        self.size = size
        self.aliens = [["👽"] * size for _ in range(size // 2)]

    def damage_taken(self, coordinate_x):
        for alien_row in reversed(self.aliens):
            if alien_row[coordinate_x] in ("⬛","💀"):
                alien_row[coordinate_x] = "💥"
            elif alien_row[coordinate_x] == "👽":
                alien_row[coordinate_x] = "💀"
                break


    def clear_alien_rows(self):
        for i, row in enumerate(self._aliens):
            for j, cell in enumerate(row):
                if cell in ("💀", "💥"):
                    self._aliens[i][j] = "⬛"

    def has_alien(self, coordinate_y, coordinate_x):
        return self.aliens[coordinate_y][coordinate_x] == "👽"

    @property
    def aliens(self):
        return self._aliens

    @aliens.setter
    def aliens(self, aliens):
        self._aliens = aliens