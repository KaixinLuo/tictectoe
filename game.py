import core
import player

class Game:

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
        self.firsthand=player.Human(core.FIRST_HAND)
        self.lasthand=player.Bot(core.LAST_HAND)

    def initialize(self):
        if (input("do you would like to take the first hand?(y/n)")=='n'):
            self.firsthand = player.Bot(core.FIRST_HAND)
            self.lasthand = player.Human(core.LAST_HAND)

    def ply(self):
        """
        make a ply

        Parameters:
        """
        core.print_board(self.board)
        is_first_hand_turn = True
        while(core.is_playable(self.board)):
            if (is_first_hand_turn):
                self.firsthand.play(self.board)
            else :
                self.lasthand.play(self.board)
            is_first_hand_turn = not is_first_hand_turn
        else:
            (_,winner) = core.get_game_state(self.board)
            if (winner == self.firsthand.label):
                print ("first hand win")
            elif(winner == self.lasthand.label):
                print("last hand win")
            else:
                print ("tie!")
