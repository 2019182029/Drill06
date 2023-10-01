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

def draw_hand() :
    for i in range(0, hands) :
        hand.draw(hand_x[i - 1], hand_y[i - 1])

def cha_move(t) :
    global cha_x, cha_y

    cha_x = (1 - t) * cha_x + t * hand_x[0]
    cha_y = (1 - t) * cha_y + t * hand_y[0]

while(running) :
    for i in range(0, 100 + 1, 4) :
        clear_canvas()

        ground.draw(ground_width // 2, ground_height // 2)
        
        handle_events()

        character.clip_draw(frame * 100, 0, 100, 100, cha_x, cha_y)

        if(hands != 0) :
            t = i / 100
            draw_hand()
            cha_move(t)
            
        update_canvas()

        frame = (frame + 1) % 8

        delay(0.1)

close_canvas()