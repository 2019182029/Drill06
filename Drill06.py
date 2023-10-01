from pico2d import *

ground_width, ground_height = 1280, 1024
running = True
frame = 0
hand_x, hand_y = [], []
hands = 0
cha_x, cha_y = ground_width // 2, ground_height // 2

open_canvas(ground_width, ground_height)

ground = load_image('TUK_GROUND.png')
character = load_image('character.png')
hand = load_image('hand_arrow.png')

def handle_events() :
    global running
    global hand_x, hand_y
    global hands

    events = get_events()
    for event in events :
        if(event.type == SDL_QUIT) :
            running = False
        elif(event.type == SDL_MOUSEBUTTONDOWN) :
            hand_x.append(event.x)
            hand_y.append(ground_height - 1 - event.y)
            hands += 1
        elif(event.type == SDL_KEYDOWN) :
            if(event.key == SDLK_ESCAPE) :
                running = False
    

while(running) :
    clear_canvas()

    ground.draw(ground_width // 2, ground_height // 2)
    
    handle_events()

    for i in range(0, hands) :
        hand.draw(hand_x[i - 1], hand_y[i - 1])

    update_canvas()
        
    frame = (frame + 1) % 8

    delay(0.1)

close_canvas()