import simplegui as sg

#global variables
time_count = 0
status = False
all_attempts = 0
succes_attempts = 0

def percentage(s_a,all_a):
    if s_a == 0 and all_a == 0:
        return '0%'
    per = (s_a * 100)/ all_a
    return str(per)+'%'

#define counter attemps function
def counter_stop(succes,all):
    global all_attempts, succes_attempts
    return str(succes_attempts)+'/'+str(all_attempts)
      

#define helper function format that convert time 
#in tenths of seconds into formatted string A:BC.D
def format(t):
    res = ''
    d = t % 10
    c = t / 10
    c = c % 10
    b = t / 100
    b = b % 6 
    a = (t / 100) / 6
    if a == 10:
        timer.stop()
        return 'Time over!'
    res += str(a) + ':' + str(b) + str(c) +'.'+ str(d)
    return res
    

#define event handlers for buttons: 'Start', 'Stop', 'Reset'
def start_button_handler():
    global status
    timer.start()
    status = True

def stop_button_handler():
    global status, succes_attempts, all_attempts
    if time_count%10 == 0 and status == True:
        succes_attempts += 1
        all_attempts += 1
    elif time_count%10 != 0 and status == True:
        all_attempts += 1    
    status = False
    
def reset_button_handler():
    global time_count, succes_attempts, all_attempts
    time_count = 0
    succes_attempts = 0
    all_attempts = 0
    timer.stop() 
    
#define event handler for timer with 0.1 sec interval
def create_timer():
    if status:
        global time_count
        time_count += 1
    else:
        timer.stop()

#define draw handler
def draw(canvas):
    canvas.draw_text(format(time_count),[100,160],45, 'White')
    canvas.draw_text(counter_stop(succes_attempts,all_attempts), [230,40], 30, 'White')
    
    text = percentage(succes_attempts,all_attempts)
    if int(text[:-1]) < 50 and int(text[:-1]) >= 30:
        canvas.draw_text(text,[40,40],30,'Silver')
    elif int(text[:-1]) < 30:
        canvas.draw_text(text,[40,40],30,'Gray')
    elif int(text[:-1]) >= 50 and int(text[:-1]) < 70:
        canvas.draw_text(text,[40,40],30,'Green')  
    elif int(text[:-1]) >= 70 and int(text[:-1]) < 85:
        canvas.draw_text(text,[40,40],30,'Purple')
    elif int(text[:-1]) >= 85 and int(text[:-1]) < 100:
        canvas.draw_text(text,[40,40],30,'Fuchsia')
    elif int(text[:-1]) == 100:  
        canvas.draw_text(text,[40,40],30,'Aqua')

#create frame
frame = sg.create_frame('Stopwatch',300,300)

#register event handlers
frame.set_draw_handler(draw)
timer = sg.create_timer(100, create_timer)
start_button = frame.add_button('Start', start_button_handler,70)
stop_button = frame.add_button('Stop', stop_button_handler,70)
reset_button = frame.add_button('Reset', reset_button_handler,70)


#start frame
frame.start()
#timer.start()
print timer.is_running()