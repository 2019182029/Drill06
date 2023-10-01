from pico2d import *

ground_width, ground_height = 1280, 1024
running = True
frame = 0
hand_x, hand_y = [], []
cha_x, cha_y = ground_width // 2, ground_height // 2

open_canvas(ground_width, ground_height)

ground = load_image('TUK_GROUND.png')
character = load_image('character.png')
hand = load_image('hand_arrow.png')

def handle_events() :
    global running

    events = get_events()
    for event in events :
        if(event.type == SDL_QUIT) :
            running = False
        elif(event.type == SDL_KEYDOWN) :
            if(event.key == SDLK_ESCAPE) :
                running = False
    

while(running) :
    clear_canvas()

    ground.draw(ground_width // 2, ground_height // 2)

    handle_events()

    update_canvas()
        
    frame = (frame + 1) % 8

    delay(0.1)

close_canvas()
