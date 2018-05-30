
def get_avaliable_policy(board):
    return [x for x in range(9) if board[x]==0]

# this is not correct
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