import ai
import core 

class Bot:
    def __init__(self,label):
        self.label = label
    
    def play(board):
        own_vision=[i/self.label for i in board]
        (policy,util)=ai.best_policy_and_util(own_vision)
        board[policy]=self.label

class Human(object):
    def __init__ (self,label):
        self.label = label
    def play(board):
        while (policy = int(input("please take you action:"))>8):
            print("Action is not valid, try another one:")
        board[policy]=self.label
        