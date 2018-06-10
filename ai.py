import math
import core

def available_policy(board):
    return [x for x in range(9) if board[x]==0]

def best_policy_and_util(board):
    possible_policies =available_policy(board)
    best_policy = -1
    
    (has_empty,winner)=core.get_game_state(board)
    max_util = winner*10
    if (has_empty and winner == 0 ):
        for policy in possible_policies:
            image_board = core.apply_policy(board,policy,core.ENEMY)
            (_ , temp_util) = worst_policy_and_util(image_board)
            if(temp_util>max_util):
                best_policy = policy
                max_util=temp_util
    return (best_policy,max_util)

def worst_policy_and_util(board):
    possible_policies = available_policy(board)
    worst_policy = -1
    
    (has_empty,winner)=core.get_game_state(board)
    min_util = -winner*10
    if (has_empty and winner == 0 ):
        for policy in possible_policies:
            image_board = core.apply_policy(board,policy,core.SELF)
            (_ , temp_util) =best_policy_and_util(image_board)
            if(temp_util<min_util):
                worst_policy = policy
                min_util=temp_util
    return (worst_policy,min_util)

def max_utility(board):
    """
    Returns the max utility value given a board

    Parameters:
    board (list): A list of size 9 representing the game board in finished state

    Returns:
    int: the maximum utility values generated by possible plies
    """
    state = core.get_game_state(board)
    if state[0] != 1 or state[1] != 0:
        return utility(board)
    else:
        value = -math.inf
        for action in available_policy(board):
            value = max(value, min_utility(core.apply_policy(board, action, 1)))
        return value

def min_utility(board):
    """
    Returns the min utility value given a board

    Parameters:
    board (list): A list of size 9 representing the game board in finished state

    Returns:
    int: the maximum utility values generated by possible plies
    """
    state = core.get_game_state(board)
    if state[0] != 1 or state[1] != 0:
        return utility(board)
    else:
        value = math.inf
        for action in available_policy(board):
            value = min(value, max_utility(core.apply_policy(board, action, -1)))
        return value

def utility(board):
    """
    Returns the utility value of the board given a finished board

    Parameters:
    board (list): A list of size 9 representing the game board in finished state

    Returns:
    int: 10 if the first hand wins, -10 if the last hand wins
         0 if it's a time
    """
    state = core.get_game_state(board)
    if state[1] == 1:
        return 10
    elif state[1] == -1:
        return -10
    else:
        return 0
