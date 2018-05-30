#the ai is 1 and enemy is -1
FIRST_HAND=1
LAST_HAND=-1

def new_board():
    return [0]*9

def update_board(board,policy,player_flag):
    result = [i for i in board]
    if (result[policy]==0):
        result[policy]=player_flag
    else:
        print("you are placing a chess on a unavaliable position")
    return result#since we have to try the possible policy,this will return a new board with updated info

def get_avaliable_policy(board):
    return [x for x in range(9) if board[x]==0]

def who_is_win(board):
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
    return ((0 in board),who_is_win(board))

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
    