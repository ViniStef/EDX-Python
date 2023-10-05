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