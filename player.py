import ai
import core 

class Bot:
    def __init__(self,label):
        self.label = label
    
    def play(board):
        own_vision=[i/self.label for i in board]
        (policy,util)=best_policy_and_util(own_vision)
        board[policy]=self.label

class human_player(object):
    def __init__ (self,label):
        self.label = label
    def play(board):
        print ("please take you action:")
        while (policy = int(input())>8):