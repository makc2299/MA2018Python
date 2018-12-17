# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
true_click = 0 

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_object = []	# create Hand object

    def __str__(self):
        ans = 'Hand contains '
        for i in range(len(self.hand_object)):	# return a string representation of a hand
            ans += str(self.hand_object[i])+' ' 	
        return ans
        
    def add_card(self, card):
        self.hand_object.append(card)	# add a card object to a hand

    def get_value(self):
        hand_value = 0
        ace = False
        for object in self.hand_object:
            if object.rank != 'A':
                hand_value += VALUES[object.rank]
            else:
                hand_value += VALUES[object.rank]
                ace = True    
        if not ace:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value 
    def draw(self, canvas,pos):
        i = 0
        for object in self.hand_object:    # draw a hand on the canvas, use the draw method for cards
            object.draw(canvas,pos)
            pos[0] += CARD_SIZE[0]
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_object = []
        [[ self.deck_object.append( Card(SUITS[i] ,RANKS[j])) for j in range(len(RANKS))] for i in range(len(SUITS))]	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_object)   # use random.shuffle()

    def deal_card(self):
        card = self.deck_object.pop()
        return card
    
    def __str__(self):
        ans = 'Deck contains '
        for i in range(len(self.deck_object)):	
            ans += str(self.deck_object[i])+' ' 	
        return ans	# return a string representing the deck

#define event handlers for buttons
def deal():
    global outcome, in_play, new_player, dealer, obj1, true_click ,score
    outcome = "Hit or stand?"
    true_click = 0 
    obj1 = Deck()
    obj1.shuffle()
    new_player = Hand()
    dealer = Hand()
    for i in range(2):
        new_player.add_card(obj1.deal_card())
        dealer.add_card(obj1.deal_card())
    if in_play:
        score -= 1
    in_play = True

def hit():
    global outcome, in_play, score,true_click 
    if in_play:
        if new_player.get_value() <= 21:
            new_player.add_card(obj1.deal_card()) 
            if new_player.get_value() > 21:
                outcome = "You have busted.New deal?" 
                in_play = False
                score -= 1
                true_click += 1

def stand():
    global in_play, outcome, score, true_click
    if true_click == 0:        
        while dealer.get_value() < 17:
            dealer.add_card(obj1.deal_card())
        if dealer.get_value() > 21:    
            outcome = "Dealer busted,you win.New deal?"
            score += 1
            true_click += 1
        elif dealer.get_value() >= new_player.get_value():
            outcome = "Dealer win.New deal?"
            score -= 1
            true_click += 1
        else:
            outcome = "You win.New deal?"
            score += 1
            true_click += 1
        in_play = False

# draw handler    
def draw(canvas):
    canvas.draw_text(outcome, [50, 80], 25, 'Black')
    canvas.draw_text('BlackJack', [250, 40], 35, 'Black')
    canvas.draw_text('Score '+str(score), [50, 58], 24, 'Black')
    new_player.draw(canvas,[0, 300])
    dealer.draw(canvas,[0, 100])
    if in_play:
        canvas.draw_image(card_back,CARD_BACK_CENTER,CARD_BACK_SIZE,[CARD_CENTER[0],CARD_CENTER[1] + 100] ,CARD_BACK_SIZE)  

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
