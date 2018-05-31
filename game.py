import core

class game:

    """
    class representing a game state for tic-tac-toe

    Attributes:
        board (list): A list of size 9 representing the game board
        player (int): the number indicating the current player, 1 for X, 2 for O
    """

    def __init__(self):
        """
        create a new game
        """
        self.board = core.new_board()
        self.player = 1
