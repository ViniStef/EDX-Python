from pyfiglet import Figlet
from alien import Alien
from board import Board
from spaceship import Spaceship

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