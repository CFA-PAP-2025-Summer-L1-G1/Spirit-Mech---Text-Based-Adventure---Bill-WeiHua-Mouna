from game_funcs import *
import game_engine
import random
from random import randint
mrun = 0
brun = 0
user_input = ""
printed_text = print_text(user_input, 30)

#Set this first to decide the world dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spirit-Mech")

#Below is where most of your code will be written

# Title Screen
add_background("spiritmech.png")

play_button = print_text("Play", 100)
place_element(play_button, 320, 350)
def clicked_play_button(play_button):
    remove_el(play_button)
    add_background("black.png")
    place_element(printed_text, 100, 400)
    #pygame.mixer.music.load("audio/chiptune.mp3")
    #pygame.mixer.music.play(loops=-1)
    mecha_dragon()
    # global startpoint
    # list = [1,2,3]
    # startpoint = list.pop()
    # if startpoint == 1:
    #     best_buddy()
    # if startpoint == 2:
    #     wandering_family()
    # if startpoint == 3:
    #     mecha_dragon()

# Characters
def best_buddy(): # Summons best buddy
    global brun
    brun = 1
    global best_buddy_image
    global best_buddy_dialogue
    best_buddy_image = add_image("alien.png") # Placeholder image
    add_image("textbox.png")
    place_element(best_buddy_image, 1, 1)
    best_buddy_dialogue = print_text("Something", 30) # Placeholder dialogue
    place_element(best_buddy_dialogue, 320, 400)
    
def best_buddy_option():
    if "x" in user_input: # X is placeholder for option 1
        remove_el(best_buddy_image)
        remove_el(best_buddy_dialogue)
        brun = 0
        best_buddy_option1 = print_text("Heading X", 30)
        place_element(best_buddy_option1, 320, 300)
        return

    elif "y" in user_input: # Y is a placeholder for option 2
        remove_el(best_buddy_image)
        remove_el(best_buddy_dialogue)
        brun = 0
        best_buddy_option2 = print_text("Heading this way I guess", 30)
        place_element(best_buddy_option2, 320, 300)
        return
        
def mecha_dragon(): # Summons Mecha Dragon
    global mrun
    mrun = 1
    mecha_dragon_image = add_image("mechadragon.png") # the mecha dragon img
    place_element(mecha_dragon_image, 1, 1)
    resize_image(mecha_dragon_image, 800)
    mecha_dragon_dialogue = print_text("YOU THERE!!! You, who have stolen that powerful mech. I shall forcibly take it from your hands!", 30)
    place_element(mecha_dragon_dialogue, 100, 350)
    mecha_dragon_option = print_text("If you really want it. Be ready to forefit your life, Dragon!", 40)
    place_element(mecha_dragon_option, 320, 400)
    add_image("textbox.png")
    
    def clicked_mecha_dragon_option(mecha_dragon_option): # Button to remove dialogue & option
        global fight_intruction
        remove_el(mecha_dragon_option)
        remove_el(mecha_dragon_dialogue)
        fight_intruction = print_text("What will you do?", 30)
        place_element(fight_intruction, 320, 400)

    click(mecha_dragon_option, clicked_mecha_dragon_option) # Calls the button to remove dialogue/option

def try_again_button(try_again): # The try again button function
    remove_el(result_dialogue)
    remove_el(result_text)
    remove_el(try_again)
    fight_intruction = print_text("What will you do?", 30)
    place_element(fight_intruction, 320, 400)
    mecha_dragon_fight_option()

# global mecha_dragon_fight_option
def mecha_dragon_fight_option(): # The player's option
    global result_dialogue
    global result_text
    global try_again
    
    if "fight" in user_input: # The results of fight
        remove_el(fight_intruction)
        result = random.choice(["Win", "Win", "Win", "Lose"])
        
        if result == "Win": # Winning the fight
            result_text = print_text("You defeated the Mecha-Dragon!", 40)
        
        else: # Losing the fight
            result_text = print_text("You suffered an crushing defeat!", 40)
        
        place_element(result_text, 50, 300)
        
    elif "defend" in user_input: # The results of defend
        remove_el(fight_intruction)
        result = random.choice(["Win", "Win", "Lose", "Lose", "Lose"])
        
        if result == "Win": # Winning the defend
            result_dialogue = random.choice(["A", "B", "C"])
        
            if result_dialogue == "A":
                result_text = print_text("You successfully defended against powerful blow!", 20)
                update_text(fight_intruction, "What will you do next?")
        
            elif result_dialogue == "B":
                result_text = print_text("You managed to block an heavy attack!", 20)
                update_text(fight_intruction, "What will you do next?")
        
            elif result == "C":
                result_text = print_text("You closely dodged a huge fire breath!", 20)
                update_text(fight_intruction, "What will you do next?")

            place_element(result_text, 50, 300)
        
        else: # Losing the defend
            result_dialogue = random.choice(["A", "B", "C"])
        
            if result_dialogue == "A":
                result_text = print_text("You suffered an heavy blow!", 20)
                update_text(fight_intruction, "What will you do next?")
        
            elif result_dialogue == "B":
                result_text = print_text("You are hurt!", 20)
                update_text(fight_intruction, "What will you do next?")
        
            elif result_dialogue == "C":
                result_text = print_text("You got burnt!", 20)
                update_text(fight_intruction, "What will you do next?")
            
            place_element(result_text, 50, 300)
    
    elif "something" in user_input: # The results of something
        result_dialogue = random.choice(["A", "B", "C"])
        
        if result_dialogue == "A":
            result_text = print_text("You threw a rock... It bounced off... What did you think would happen...", 20)
            update_text(fight_intruction, "Maybe try something smarter...")
        
        elif result_dialogue == "B":
            result_text = print_text("You faked your death... It did nothing.", 20)
            update_text(fight_intruction, "Why did you think that would work... Try again")
        
        elif result_dialogue == "C":
            result_text = print_text("You pleaded, begged... but the dragon is cold-hearted...", 20)
            update_text(fight_intruction, "COWARD! FIGHT!")

        remove_el(fight_intruction)
        place_element(result_text, 50, 300)
        try_again = print_text("Try Again", 30)
        place_element(try_again, 500, 500)
        click(try_again, try_again_button)
    
    elif "run" in user_input: # The result of run
        sys.exit()
            

def wandering_family(): # Introduces the Wandering Family To The Game 
    global wandering_family_image
    global wandering_family_dialogue
    wandering_family_image = add_image("dino.gif") #place holder for now 
    add_image("textbox.png")
    place_element(wandering_family_image, 1, 1)
    wandering_family_dialogue = print_text("A wandering family of 3 asks for spirit-fuel to keep their house running.", 30)
    place_element(wandering_family_dialogue, 100, 200)
    
# global wandering_family_option # Introduces the user to an option of giving spirit fuel, or declining
def wandering_family_option():
    if "yes" in user_input:
        remove_el(wandering_family_dialogue)
        add_image("asteroid.png") #place holder for now
        accepted_option_text = print_text("Thank you, traveler. May the gods be with you on this journey.", 30)
        place_element(accepted_option_text, 60, 300)
    elif "no" in user_input:
        remove_el(wandering_family_dialogue)
        add_image("wall.png") #place holder for now
        refused_option_text = print_text("Sorry about bothering you. No worries.", 30)
        place_element(refused_option_text, 60, 300)
    

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

# User Input Functions
def submitted_input():
    global user_input
    if "quit" in user_input:
        sys.exit()
    # if "north" in user_input: # go north
    #     submitted_text = print_text("detected north", 30)
    #     place_element(submitted_text, 320, 300)
    # if startpoint == 1:
    #     best_buddy_option()
    #     startpoint = 2 # code to move to the next path
    # if startpoint == 2:
    #     mecha_dragon_fight_option()
    #     startpoint = 3 # code to move to the next path
    # if startpoint == 3:
    #     wandering_family_option()
    #     # code to move to the next path
    mecha_dragon_fight_option()
    
def upd_input(event):
    global user_input
    global printed_text
    if event.key == pygame.K_BACKSPACE:
        user_input = user_input[:-1]  # Remove last character
    elif event.key == pygame.K_RETURN:
        submitted_input()
        user_input = ''
    else:
        user_input += event.unicode.lower()  # Add character
    update_text(printed_text, user_input)

# Function Calls

click(play_button, clicked_play_button)

#DO NOT EDIT BELOW 
game_engine.start(update, upd_input)