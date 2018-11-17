import simplegui 
import random
import math

num_range = 100
secret_number = 0
user_guess = 0
num_guesses = 7

def new_game():
    global secret_number, num_range, num_guesses
    secret_number = random.randrange(0,num_range)
    if num_range == 100:
        num_guesses = 7
    elif num_range == 1000:
        num_guesses = 10
    print '\nNew game with a radius of 0 to '+str(num_range)
    print 'With the number of attempts '+str(num_guesses)

def remaining_guess():
    global num_guesses
    num_guesses-= 1
    if num_guesses > 0:
        print 'You still have '+str(num_guesses)+ ' attempts'
    else:
        print 'Sorry, you lose.The number was '+str(secret_number)
        new_game()

def input_guess(guess):
    global user_guess , secret_number
    user_guess = int(guess)
    flag = 0
    print '\nGuess was '+str(user_guess)
    if secret_number == user_guess:
        flag = 1
        print 'Correct'
        new_game()
        
    elif secret_number > user_guess:
        print 'Higher'
    elif secret_number < user_guess:
        print 'Lower'
    else:
        print 'Something went wrong'
    if flag != 1:
        remaining_guess()    
        
def range_100():
    global num_range
    num_range = 100
    print '\nYou selected a range of numbers from 0 to 100'
    new_game()
    
def range_1000():
    global num_range
    num_range = 1000
    print '\nYou selected a range of numbers from 0 to 1000'
    new_game()
        
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

frame.add_button('Rangeis[0,100)',range_100,110)
frame.add_button('Rangeis[0,1000)',range_1000,110)
frame.add_input('Enter guess',input_guess,100)

new_game()
frame.start()
