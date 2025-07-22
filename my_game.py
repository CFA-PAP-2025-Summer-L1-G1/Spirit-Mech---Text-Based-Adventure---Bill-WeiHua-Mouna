from game_funcs import *
import game_engine
import random
user_input = ""
printed_text = print_text(user_input, 30)

#Set this first to decide the world dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spirit-Mech")

#Below is where most of your code will be written

add_background("spiritmech.png")

play_button = print_text("Play", 100)
place_element(play_button, 320, 350)
def clicked_play_button(play_button):
    remove_el(play_button)
    add_background("black.png")
click(play_button, clicked_play_button)

# Characters
def mecha_dragon(): 
    mecha_dragon_image = add_image("mechadragon.png")
    place_element(mecha_dragon_image, 1, 1)
    resize_image(mecha_dragon_image, 800)
    mecha_dragon_dialogue = print_text("YOU THERE!!! You, who have stolen that powerful mech. I shall forcibly take it from your hands!", 30)
    place_element(mecha_dragon_dialogue, 100, 350)
    mecha_dragon_option = print_text("If you really want it. Be ready to forefit your life!", 40)
    place_element(mecha_dragon_option, 320, 400)
    def clicked_mecha_dragon_option(mecha_dragon_option):
        remove_el(mecha_dragon_option)
        remove_el(mecha_dragon_dialogue)
        def mecha_dragon_fight():
            fight_button = print_text("Fight!", 50)
            place_element(fight_button, 220, 400)
            def clicked_fight_button(fight_button):
                fight_result = random.choice(["Win", "Win", "Win", "Lose"])
                if fight_result == "Win":
                    fight_result_text = print_text("You defeated the Mecha-Dragon!", 40)
                else:
                    fight_result_text = print_text("You suffered an crushing blow!", 40)
                place_element(fight_result_text, 50, 300)
                remove_el(fight_button)
            click(fight_button, clicked_fight_button)
        mecha_dragon_fight()
    click(mecha_dragon_option, clicked_mecha_dragon_option)



rooms = [
    {
        "description": "You are in a dark room.",
        "actions": ["Go east", "Go west"]
    },
    {
        "description": "You are in a brightly lit room.",
        "actions": ["Go west", "Go north"]
    },
    {
        "description": "You are in a narrow hallway.",
        "actions": ["Go south", "Go east"]
    }
]

current_room = 0

# room_description, room_rect = print_text(rooms[current_room]["description"], 36)
# room_rect.topleft = (20, 20)
# screen.blit(room_description, room_rect)

# for i, action in enumerate(rooms[current_room]["actions"]):
#     action_text, action_rect = print_text(action, 24)
#     action_rect.topleft = (20, 80 + 30 * i)
#     screen.blit(action_text, action_rect)

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

def submitted_input():
    global user_input
    if "north" in user_input: # go north
        submitted_text = print_text("detected north", 30)
        place_element(submitted_text, 320, 300)
        user_input = ''
        

def upd_input(event):
    global user_input
    global printed_text
    if event.key == pygame.K_BACKSPACE:
        user_input = user_input[:-1]  # Remove last character
    elif event.key == pygame.K_RETURN:
        submitted_input()  # Enter is pressed 
    else:
        user_input += event.unicode  # Add character
    update_text(printed_text, user_input)
    
#DO NOT EDIT BELOW 
game_engine.start(update, upd_input)