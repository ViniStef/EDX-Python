import sys
from pyfiglet import Figlet


class Screen_render:
    ...


class Game:
    COMMAND_LEFT = "A"
    COMMAND_RIGHT = "D"
    COMMAND_SHOOT = "S"
    figlet = Figlet()

    def __init__(self, alien, spaceship, board) -> None:
        self.alien = alien
        self.spaceship = spaceship
        self.board = board

    def game_start(self):
        for i in self.board.board:
            print(i)
        while not self.game_over():
            command = (
                input(
                    "Input 'A' to move left, 'D' to move right, or type 'S' to shoot: "
                )
                .strip()
                .upper()
            )
            self.cmd_handler(command)
            self.board.print_board()
        self.figlet.setFont(font="slant")
        print(self.figlet.renderText("Game Over"))

    def cmd_handler(self, cmd):
        if cmd == self.COMMAND_LEFT:
            self.spaceship.coordinate_x -= 1
        elif cmd == self.COMMAND_RIGHT:
            self.spaceship.coordinate_x += 1
        elif cmd == self.COMMAND_SHOOT:
            shoot_action = self.spaceship.shoot(self.spaceship.coordinate_x)
            self.board.handle_shots(shoot_action)
            self.alien.damage_taken(self.spaceship.coordinate_x)
        if cmd in (self.COMMAND_LEFT, self.COMMAND_RIGHT):
            self.spaceship.move(self.spaceship.coordinate_x)
            self.board.reset_paralel_rows()
            self.alien.clear_alien_rows()

    def game_over(self):
        for alien_row in self.alien.aliens:
            if "👽" in alien_row:
                return False
            else:
                return True

    @classmethod
    def get(cls):
        size = 3
        while True:
            try:
                game_size = int(
                    input(
                        "How big should the game board be? (Minimum size is 3,odd numbers only): "
                    ).strip()
                )
                break
            except ValueError:
                pass

        if game_size % 2 != 1:
            game_size += 1
        if game_size >= 3:
            size = game_size

        alien = Alien(size)
        spaceship = Spaceship(int(size % 2 + (size // 2)) - 1, size)
        board = Board(alien, spaceship, size)
        return cls(alien, spaceship, board)


class Board:
    def __init__(self, aliens, ship, size=3) -> None:
        self.aliens = aliens
        self.ship = ship
        self.size = size
        self.paralel_rows = [["⬛"] * size for _ in range(size // 2)]
        self.board = []

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        board = []
        for alien_row in self.aliens.aliens:
            board.append(alien_row)
        board.extend(self.paralel_rows)
        board.append(self.ship.ship)
        self._board = board

    def reset_paralel_rows(self):
        for row_index, row_value in enumerate(self.paralel_rows):
            for individual_index, individual_value in enumerate(row_value):
                if individual_value == "💥":
                    self.paralel_rows[row_index][individual_index] = "⬛"

    def handle_shots(self, shoot_tuple):
        coordinate_x, damage = shoot_tuple
        for i in reversed(range(len(self.paralel_rows))):
            self.paralel_rows[i][coordinate_x] = "💥"

    def print_board(self):
        for i in self.board:
            print(i)


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


game = Game.get()
game.game_start()
