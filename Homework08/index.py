"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 2         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def help_max_find(board,scores):
    '''This function finds the maximum in scores'''
    max_v = -float("inf")
    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if scores[row][col] > max_v and board.square(row, col) == provided.EMPTY:
                max_v = scores[row][col]        
    return max_v 

def board_check_empty(board):
    '''check board'''
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) == provided.EMPTY:
                return True
    
def get_best_move(board,scores):
    '''The function find all of the empty squares with 
        the maximum score and randomly return one of them'''
    if board_check_empty(board):

        idx_max_scores = []
        max_v = help_max_find(board,scores)
        print max_v
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == provided.EMPTY and scores[row][col] == max_v:
                    idx_max_scores.append((row,col))
        return random.choice(idx_max_scores)            

            
def mc_update_scores(scores,board,player):
    '''The function should score 
        the completed board and update the scores grid'''
    if board.check_win() == player:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == player:
                    scores[row][col]+= SCORE_CURRENT
                elif board.square(row, col) == provided.switch_player(player):
                    scores[row][col]-= SCORE_OTHER
    elif board.check_win() == provided.switch_player(player):
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == player:
                    scores[row][col]-= SCORE_CURRENT
                elif board.square(row, col) == provided.switch_player(player):
                    scores[row][col]+= SCORE_OTHER
    
def mc_trial(board,player):
    '''The function  play a game starting 
        with the given player by making random moves'''
    idx = board.get_empty_squares()
    while board.check_win() == None:
        position = random.choice(idx)
        if board.square(position[0], position[1]) == provided.EMPTY:
            board.move(position[0], position[1], player)
            player = provided.switch_player(player)
        idx.remove(position)
    print board    
            

def mc_move(board,player,trials):
    ''' The function use the Monte Carlo simulation'''
    scores = [[0 for _ in range(board.get_dim())]
              for _ in range(board.get_dim())]
    print board
    for _ in range(trials):
        board1 = board.clone()
        mc_trial(board1,player)
        mc_update_scores(scores, board1, player)
        print scores
        print board1.check_win()
    return get_best_move(board,scores)    

    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
