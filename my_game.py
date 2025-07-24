from game_funcs import *
import game_engine
import random
from random import randint

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
    #pygame.mixer.music.set_volume(0.1) 
    best_buddy()

# Characters
def best_buddy(): # Summons best buddy
    global best_buddy_image
    global best_buddy_dialogue
    best_buddy_image = add_image("alien.png") # Placeholder image
    add_image("textbox.png")
    place_element(best_buddy_image, 1, 1)
    best_buddy_dialogue = print_text("Hey there traveler! You heading 'South' or 'North' from here?", 30) # Placeholder dialogue
    place_element(best_buddy_dialogue, 100, 300)
    
def best_buddy_option():
    global best_buddy_option1
    global next
    if "north" in user_input: 
        best_buddy_option1 = print_text("Heading North! Me too! ('next')", 30)
        place_element(best_buddy_option1, 280, 300)
        next = "boss"

    elif "south" in user_input:
        best_buddy_option1 = print_text("Heading South, I assume you don't mind if I tag along? ('next')", 30)
        place_element(best_buddy_option1, 80, 300)
        next = "family"

        
def mecha_dragon(): # Summons Mecha Dragon
    mecha_dragon_image = add_image("mechadragon.png") # the mecha dragon img
    place_element(mecha_dragon_image, 1, 1)
    resize_image(mecha_dragon_image, 800)
    global mecha_dragon_dialogue
    mecha_dragon_dialogue = print_text("YOU THERE!!! You, who have stolen that powerful mech. I shall forcibly take it from your hands!", 10)
    place_element(mecha_dragon_dialogue, 50, 350)
    mecha_dragon_option = print_text("If you really want it. Be ready to forefit your life, Dragon!", 10)
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
        remove_el(fight_intruction)
        add_image("gameover.png")


def wandering_family(): # Introduces the Wandering Family To The Game 
    global wandering_family_image
    global wandering_family_dialogue
    wandering_family_image = add_image("dino.gif") #place holder for now 
    add_image("textbox.png")
    place_element(wandering_family_image, 1, 1)
    wandering_family_dialogue = print_text("Please kind sir, please spare some spirit fuel for this poor family. (accept/decline)", 25)
    place_element(wandering_family_dialogue, 80, 300)
    
# global wandering_family_option # Introduces the user to an option of giving spirit fuel, or declining
def wandering_family_option():
    global wandering_family_option_text, wandering_family_option_image
    if "accept" in user_input:
        wandering_family_option_image = add_image("asteroid.png") #place holder for now
        wandering_family_option_text = print_text("Ahh, traveler, I got hit by the 'boss'. Don't 'fight' it! Defend all you can!", 30)

    elif "decline" in user_input:
        # global starttime
        # global delay
        # delay = 2500
        wandering_family_option_text = print_text("Sorry to bother.. SOMETHING will happen to you soon...", 30)
        # starttime = pygame.time.get_ticks()
        pygame.time.delay(2500)
        clear()
        add_background("gameover.png")
    place_element(wandering_family_option_text, 60, 300)
    place_element(wandering_family_option_image, 320, 300)

    

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    # current_ticks = pygame.time.get_ticks()
    # if current_ticks - starttime >= delay:
    #     clear()
    #     add_background("gameover.png")
    pass

# User Input Functions
def submitted_input():
    global user_input
    if "quit" in user_input:
        sys.exit()
    if "shut up" in user_input:
        pygame.mixer.music.stop()
    if "north" in user_input or "south" in user_input:
        remove_el(best_buddy_image)
        remove_el(best_buddy_dialogue)
        best_buddy_option()
        # if next == "boss":
        #     remove_el(wandering_family_option_text)
        #     remove_el(wandering_family_option_image)
        #     mecha_dragon()
        # if next == "family":
        #     remove_el(best_buddy_option1)
        #     wandering_family()
    
    if "next" in user_input:
        remove_el(best_buddy_option1)
        wandering_family()

    if "accept" in user_input or "decline" in user_input:
        remove_el(wandering_family_dialogue)
        remove_el(wandering_family_image)
        wandering_family_option()

    if "boss" in user_input:
            remove_el(wandering_family_option_text)
            remove_el(wandering_family_option_image)
            mecha_dragon()
    if "fight" in user_input or "defend" in user_input or "something" in user_input or "run" in user_input:
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