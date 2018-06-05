import core

class game:

    """
    class representing a game state for tic-tac-toe

    Game board coordinate:
    |0|1|2|
    |3|4|5|
    |6|7|8|

    Attributes:
        board (list): A list of size 9 representing the game board
        player (int): the number indicating the current player, 1 for X, -1 for O
    """

    def __init__(self):
        """
        create a new game
        """
        self.board = core.new_board()
        self.player = 1
        self.step = 1

    def ply(self, position):
        """
        make a ply

        Parameters:
        position (int): position range from 0 - 8
        """
        self.board = update_board(self.board, position, self.player)
        self.player = -self.player
        self.step += 1
