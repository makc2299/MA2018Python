import random as r
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == 'rock':
        player_number = 0
    elif name == 'Spock':
        player_number = 1
    elif name == 'paper':
        player_number = 2
    elif name == 'lizard':
        player_number = 3
    elif name == 'scissors':
        player_number = 4
    else:
        print 'You gave incorrect input'
    return player_number


def number_to_name(num):
    if num == 0:
        comp_name = 'rock'
    elif num == 1:
        comp_name = 'Spock'
    elif num == 2:
        comp_name = 'paper'
    elif num == 3:
        comp_name = 'lizard'
    elif num == 4:
        comp_name = 'scissors'
    else:
        print 'incorrect number'
    return comp_name


def rpsls (player_choice):
    print '\nPlayer chooses '+player_choice
    player_number = name_to_number(player_choice)
    comp_number = r.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer's choice "+comp_choice
    res = (comp_number - player_number)%5 
    if res in [1,2]:
        print 'Computer wins!'
    elif res in [3,4]:
        print 'Player wins!'
    else:
        print 'Player and computer tie!'
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors") 
