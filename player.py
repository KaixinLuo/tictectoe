import ai
import core 

class Bot:
    def __init__(self,label):
        self.label = label
    
    def play(self,board):
        own_vision=[i/self.label for i in board]
        (policy,_)=ai.best_policy_and_util(own_vision)
        board[policy]=self.label

class Human(object):
    def __init__ (self,label):
        self.label = label
    def play(self,board):
        policy = int(input("Please take you action:"))
        while(policy>8):
            policy = int(input("Action is not valid, try another one:"))
        board[policy]=self.label
        