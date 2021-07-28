import pygame
pygame.init()
from variables import *

# images
background_menu = pygame.image.load('images/background-menu.jpg')

buttons_locations = []

# draw a button
def draw_button(window, color, message, x1, y1, x2, y2):
    pygame.draw.rect(window, color, (x1, y1, x2, y2))
    text = FONT_32.render(message, True, WHITE)
    x = x1 + x2/2 - text.get_width()/2
    y = y1 + y2/2 - text.get_height()/2
    window.blit(text, (x, y))

    # Add the buttons info to a list
    buttons_locations.append([x1, y1, x2, y2, message])
    

# Draws the menu
def draw_menu(window):
    gap = 80
    window.blit(background_menu, (0, 0))
    draw_button(window, BLACK, "Hiragana", (WIDTH/2 - 100), HEIGHT/2 - gap, 200, 40)
    draw_button(window, BLACK, "Katakana", (WIDTH/2 - 100), HEIGHT/2, 200, 40)
    draw_button(window, BLACK, "Frases", (WIDTH/2 - 100), HEIGHT/2 + gap, 200, 40)
    draw_button(window, BLACK, "Kanji", (WIDTH/2 - 100), HEIGHT/2 + gap*2, 200, 40)


# Checks if a button was pressed and return True and the button pressed or False
def isPressed():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for button in buttons_locations:
        x_check = (mouse_x < button[0] + button[2] and mouse_x > button[0])
        y_check = (mouse_y < button[1] + button[3] and mouse_y > button[1])
        if x_check and y_check:
            return button[4]

    return "menu"
