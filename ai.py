import core
"""
    this file contains the core function of ai
"""

"""
    get the all possible policy
"""
def available_policy(board):
    return [x for x in range(9) if board[x]==0]

"""
    Max Method
"""
def best_policy_and_util(board,label):
    possible_policies =available_policy(board)
    best_policy = core.INIT_POLICY
    
    (has_empty,winner)=core.get_game_state(board)
    max_util = core.INIT_MAX_UTIL
    if (has_empty and winner == 0 ):
        
        for policy in possible_policies:
            image_board = core.apply_policy(board,policy,label)
            (_ , r) = worst_policy_and_util(image_board,-label)
            if(r>max_util):
                best_policy = policy
                max_util=r
    else:
        max_util = winner*10
    return (best_policy,max_util)
"""
    Min method
"""
def worst_policy_and_util(board,label):
    possible_policies = available_policy(board)
    worst_policy = core.INIT_POLICY
    
    (has_empty,winner)=core.get_game_state(board)
    min_util = core.INIT_MIN_UTIL
    if (has_empty and winner == 0 ):
        
        for policy in possible_policies:
            image_board = core.apply_policy(board,policy,label)
            (_ , temp_util) =best_policy_and_util(image_board,-label)
            if(temp_util<min_util):
                worst_policy = policy
                min_util=temp_util
    else:
        min_util = winner*10
        
    return (worst_policy,min_util)


