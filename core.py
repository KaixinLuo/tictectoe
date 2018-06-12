#the ai is 1 and enemy is -1
FIRST_HAND = 1
LAST_HAND = -1
SELF=1
ENEMY=-1
INIT_MAX_UTIL = -100
INIT_MIN_UTIL = 100
INIT_POLICY = -100
import copy
def new_board():
    """
    Return a list representing an empty board

    Returns:
    list: [0, 0, ... 0]
    """
    return [0]*9

def apply_policy(board, policy, player_flag):
    """
    Return a new updated board with board, policy, and player_flag

    Parameters:
    board (list): the list with size 9 representing the board
    policy (int): the integer representing the position of the ply
    player_flag(int): the value of the player, 1 for first hand, -1 for last hand

    Returns:
    list: a new list representing the updated board
    """
    result = copy.deepcopy(board)
    if (result[policy]==0):
        result[policy]=player_flag
    else:
        print("you are placing a chess on a unavaliable position")
    return result#since we have to try the possible policy,this will return a new board with updated info
def is_policy_avaliable(board,position):
    return (position<=8)and(board[position] == 0)

def available_ply(board):
    """
    Return a list contains all the available positions on the board

    Parameters:
    board (list): the list with size 9 representing the board

    Returns:
    list: a list containing all the positions available on the board
    """
    return [i for i in range(9) if board[i] == 0]

def who_is_win(board):
    """
    Determine whether the game ends and the winner if it ends

    Parameters:
    board(list): the list with size 9 representing the board

    Returns:
    int: 1 if first hand is the winner, -1 if the last hand is the winner,
         0 if tie or not finished
    """
    result = 0
    if (board[0]+board[1]+board[2]==3 or board[3]+board[4]+board[5]==3 or board[6]+board[7]+board[8]==3):
        result = 1
    elif (board[0]+board[1]+board[2]==-3 or board[3]+board[4]+board[5]==-3 or board[6]+board[7]+board[8]==-3):
        result = -1
    elif(board[0]+board[3]+board[6]==3 or board[1]+board[4]+board[7]==3 or board[2]+board[5]+board[8]==3):
        result = 1
    elif (board[0]+board[3]+board[6]==-3 or board[1]+board[4]+board[7]==-3 or board[2]+board[5]+board[8]==-3):
        result = -1
    elif (board[0]+board[4]+board[8]==3):
        result = 1
    elif (board[0]+board[4]+board[8]==-3):
        result = -1
    elif (board[2]+board[4]+board[6]==3):
        result = 1
    elif (board[2]+board[4]+board[6]==-3):
        result = -1
    else:
        result = 0
    return result

def get_game_state(board):
    return ((0 in board), who_is_win(board))

def is_playable(board):
    (has_empty,winner)=get_game_state(board)
    return has_empty and (winner == 0)

def print_board(board):
    format_dict = {
        0:'-',
        1:'O',
        -1:'X'
    }
    formatted_board = [format_dict[x] for x in board]
    print(formatted_board[0],formatted_board[1],formatted_board[2])
    print(formatted_board[3],formatted_board[4],formatted_board[5])
    print(formatted_board[6],formatted_board[7],formatted_board[8])
