from game_funcs import *
import game_engine
from game_engine import *

#Set this first to decide the world dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spirit-Mech")

#Below is where most of your code will be written

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()

def render_text(text, font_size, color=(255, 255, 255)):
    font = pygame.font.Font(pygame.font.get_default_font(), 12)
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

welcome_text, welcome_rect = render_text("Welcome to Text Adventure!", 48)
welcome_rect.center = (screen_width // 2, screen_height // 2)
screen.blit(welcome_text, welcome_rect)

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

room_description, room_rect = render_text(rooms[current_room]["description"], 36)
room_rect.topleft = (20, 20)
screen.blit(room_description, room_rect)

for i, action in enumerate(rooms[current_room]["actions"]):
    action_text, action_rect = render_text(action, 24)
    action_rect.topleft = (20, 80 + 30 * i)
    screen.blit(action_text, action_rect)

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

#DO NOT EDIT BELOW 
game_engine.start(update)