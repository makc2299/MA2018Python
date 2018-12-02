# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
ball_vel = [0,0]
paddle2_vel = 0
paddle1_vel = 0
LEFT = False
RIGHT = True
score1 = 0
score2 = 0

def button_handler():
    new_game()

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [ WIDTH / 2 , HEIGHT / 2]
    #ball_vel = [0,0]
    if direction == LEFT:
        ball_vel[0] = -(random.randrange(120,240))/60.0
        ball_vel[1] = -(random.randrange(60,180))/60.0
    if direction == RIGHT:
        ball_vel[0] = (random.randrange(120,240))/60.0
        ball_vel[1] = -(random.randrange(60,180))/60.0    
   

    # define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
    
    #touching the top and bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    #the ball touches/collides with the left and right gutters.
    condition_left_if_1 = ball_pos[1] >= paddle1_pos - PAD_HEIGHT / 2 - BALL_RADIUS / 2
    condition_left_if_2 = ball_pos[1] <= paddle1_pos + PAD_HEIGHT / 2 + BALL_RADIUS / 2
    condition_left_if_3 = ball_pos[0] <= PAD_WIDTH + BALL_RADIUS
    condition_left_elif_1 = ball_pos[1] < paddle1_pos - PAD_HEIGHT / 2 - BALL_RADIUS / 2 and condition_left_if_3
    condition_left_elif_2 = ball_pos[1] > paddle1_pos + PAD_HEIGHT / 2 + BALL_RADIUS / 2 and condition_left_if_3
    if condition_left_if_1 and condition_left_if_2 and condition_left_if_3:
        ball_vel[1] +=  (ball_vel[1] * 10)/100.0
        ball_vel[0] += (ball_vel[0] * 10)/100.0
        ball_vel[0] = -ball_vel[0]
        sound = random.choice([sound1,sound2,sound3])
        sound.play()
    elif condition_left_elif_1 or condition_left_elif_2:
        spawn_ball(RIGHT)
        score2 += 1
        
    condition_right_if_1 = ball_pos[1] >= paddle2_pos - PAD_HEIGHT / 2 - BALL_RADIUS / 2
    condition_right_if_2 = ball_pos[1] <= paddle2_pos + PAD_HEIGHT / 2 + BALL_RADIUS / 2
    condition_right_if_3 = ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS
    condition_right_elif_1 = ball_pos[1] < paddle1_pos - PAD_HEIGHT / 2 - BALL_RADIUS / 2 and condition_right_if_3
    condition_right_elif_2 = ball_pos[1] > paddle1_pos + PAD_HEIGHT / 2 + BALL_RADIUS / 2 and condition_right_if_3
    if condition_right_if_1 and condition_right_if_2 and condition_right_if_3:
        ball_vel[1] +=  (ball_vel[1] * 10)/100.0
        ball_vel[0] += (ball_vel[0] * 10)/100.0
        ball_vel[0] = -ball_vel[0]
        sound = random.choice([sound1,sound2,sound3])
        sound.play()
    elif condition_right_elif_1 or condition_right_elif_2:    
        spawn_ball(LEFT)
        score1 += 1
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] +=  ball_vel[0]
    ball_pos[1] +=  ball_vel[1]      
    # draw ball
    canvas.draw_circle( ball_pos, BALL_RADIUS, 10 , 'Lime', 'White' )
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos >= PAD_HEIGHT / 2:
        paddle1_pos += paddle1_vel
    else:
        paddle1_pos = PAD_HEIGHT / 2
    if paddle1_pos <= HEIGHT - PAD_HEIGHT / 2:
        paddle1_pos += paddle1_vel
    else:    
        paddle1_pos = HEIGHT - PAD_HEIGHT / 2
    
    if paddle2_pos >= PAD_HEIGHT / 2:
        paddle2_pos += paddle2_vel
    else:
        paddle2_pos = PAD_HEIGHT / 2
    if paddle2_pos <= HEIGHT - PAD_HEIGHT / 2:
        paddle2_pos += paddle2_vel
    else:    
        paddle2_pos = HEIGHT - PAD_HEIGHT / 2
        
    # draw paddles
    pos_point1_left = [PAD_WIDTH / 2, paddle1_pos + PAD_HEIGHT /2 ]
    pos_point2_left = [PAD_WIDTH / 2, paddle1_pos - PAD_HEIGHT /2 ]
    canvas.draw_line( pos_point1_left ,pos_point2_left ,PAD_WIDTH , 'White')
    
    pos_point1_right = [ WIDTH - PAD_WIDTH / 2, paddle2_pos + PAD_HEIGHT /2]
    pos_point2_right = [ WIDTH - PAD_WIDTH / 2, paddle2_pos - PAD_HEIGHT /2]
    canvas.draw_line(pos_point1_right, pos_point2_right ,PAD_WIDTH , 'White')
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [ WIDTH / 2 - 70 , 70], 40, 'White')
    canvas.draw_text(str(score2), [ WIDTH / 2 + 55 , 70], 40, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel  
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 3  
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 3
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 3
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 3
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Resets', button_handler, 70)
sound1 = simplegui.load_sound('http://dight310.byu.edu/media/audio/FreeLoops.com/5/5/Ping%20Pong.wav%20-21099-Free-Loops.com.mp3')
sound2 = simplegui.load_sound('http://www.wou.edu/~tbafarat06/1001%20Sound%20Effects/Miscellaneous/Ping%20Pong%20Ball%20on%20Table%2002.wav')
sound3 = simplegui.load_sound('http://www.wou.edu/~tbafarat06/1001%20Sound%20Effects/Miscellaneous/Ping%20Pong%20Paddle%2002.wav')
sound1.set_volume(0.6)
sound2.set_volume(0.6)
sound3.set_volume(0.6)
# start frame
new_game()
frame.start()
