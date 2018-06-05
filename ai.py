import core


def available_policy(board):
    return [x for x in range(9) if board[x]==0]

# this is not correct
'''
def get_the_best_policy(board,player_flag,opt_func = lambda x : max(x),):
    possible_policies = get_avaliable_policy(board)
    result = []
    for policy in possible_policies:
        new_board = update_board(board,policy)
        (has_empty_position,winner) = get_game_state(new_board)
        if ((not has_empty_position) or winner != 0):
            result.append((policy,winner*10/player_flag))
        else:
            (p,r)=get_the_best_policy(new_board,min if opt_func==max else max,player_flag )
            result.append((policy,r))
    return None if result == [] else opt_func(result,key=lambda x: x[1])
'''
def best_policy_and_util(board):
    possible_policies =available_policy(board)
    best_policy = -1
    
    (has_empty,winner)=core.get_game_state(board)
    max_util = winner*10
    if (has_empty and winner == 0 ):
        for policy in possible_policies:
            image_board = core.new_board(board,policy,core.ENEMY)
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
            image_board = core.new_board(board,policy,core.SELF)
            (_ , temp_util) =best_policy_and_util(image_board)
            if(temp_util<min_util):
                worst_policy = policy
                max_util=temp_util
    return (worst_policy,max_util)