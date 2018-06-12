import ai
import core 

class Bot:
    def __init__(self,label):
        self.label = label
    
    def play(self,board):
        own_vision=[i/self.label for i in board]
        #policy=ai.minimax_decision(own_vision)
        (policy,_)=ai.best_policy_and_util(own_vision,core.SELF)
        print ("AI is making decision: ", policy)
        if (core.is_policy_avaliable(board,policy)):
            board[policy]=self.label
        
        core.print_board(board)

class Human(object):
    def __init__ (self,label):
        self.label = label
    def play(self,board):
        policy = int(input("Please take you action:"))
        while(not core.is_policy_avaliable(board,policy)):
            policy = int(input("Action is not valid, try another one:"))
        board[policy]=self.label
        core.print_board(board)
        