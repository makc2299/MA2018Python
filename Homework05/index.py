# implementation of card game - Memory

import simplegui
import random

state = 0 
index_1 = []
data_struct = [[0,0] for i in range(16)] 

#function to create a deck
def random_deck_card():
    global card_deck, exposed
    res = [i for i in range(8)]
    exposed = [False for i in range(16)]
    for j in range(2):
        random.shuffle(res)
        card_deck += res

    
    
#function to create a card position    
def card_pos_creater():
    global position_pack
    positions_y = [ 100, 0, 0, 100]
    position_pack = [[ [-50,0], [-50, 0], [0, 0], [0, 0] ] for i in range(16)]
    n = 50 
    for i in range(16):
        for j in range(4):
            for k in range(1):
                position_pack[i][j][k] += n * ( i + 1)
                position_pack[i][j][k+1] = positions_y[j]

#function to combine the value, position 
#and status of the card into one structure                    
def data_structure():
    global data_struct
#    data_struct = [[0,0] for i in range(16)]          
    for i in range(16):
        for j in range(1):
            data_struct[i][0] = card_deck[i]
            data_struct[i][1] = [position_pack[i],exposed[i]]
    
    
    
# helper function to initialize globals
def new_game():
    global card_deck, exposed ,counter
    card_deck = []
    exposed = []
    counter = 0
    mouseclick_pos = 1000
    random_deck_card()
    card_pos_creater()
    data_structure()
    label.set_text('Moves = '+str(counter))
    
def comparison_card():
    global data_struct,index_1
    if len(index_1) >= 2:
        if data_struct[index_1[0]][0] != data_struct[index_1[1]][0]:
            data_struct[index_1[0]][1][1] = False
            data_struct[index_1[1]][1][1] = False
        index_1 = index_1[2:]

# define event handlers
def mouseclick(pos):
    global state, index_1, data_struct, counter
    click_pos = pos[0]    
    for i in range(16):
        if click_pos > data_struct[i][1][0][1][0] and click_pos < data_struct[i][1][0][2][0] and data_struct[i][1][1] != True:
            if state == 0:
                for i in range(16):
                    if click_pos > data_struct[i][1][0][1][0] and click_pos < data_struct[i][1][0][2][0]:
                        data_struct[i][1][1] = True
                        index_1.append(i)
                state = 1
            elif state == 1:
                for i in range(16):
                    if click_pos > data_struct[i][1][0][1][0] and click_pos < data_struct[i][1][0][2][0] :
                        data_struct[i][1][1] = True
                        index_1.append(i)                        
                state = 2
                counter += 1
                label.set_text('Moves = '+str(counter))
            else:
                for i in range(16):
                    if click_pos > data_struct[i][1][0][1][0] and click_pos < data_struct[i][1][0][2][0] :
                        data_struct[i][1][1] = True
                        index_1.append(i)                        
                comparison_card()                
                state = 1  
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    n = 1
    for i in range(16):
        if data_struct[i][1][1] == False :
            if i == 0 :
                pos = 5
            if i == 1:
                pos = 55
            canvas.draw_text( str(data_struct[i][0]), [pos, 75], 60, "White")
            pos = 50 * n
            canvas.draw_polygon(data_struct[i][1][0], 3, 'Red', 'Green')
        elif data_struct[i][1][1] == True:
            if i == 0 :
                pos = 5
            if i == 1:
                pos = 55
            canvas.draw_text( str(data_struct[i][0]), [pos, 75], 60, "White")
            pos = 50 * n
        n += 1.02


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric