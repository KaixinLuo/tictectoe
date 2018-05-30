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