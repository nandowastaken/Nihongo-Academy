import pygame
pygame.init()
from variables import *


# images
background_menu = pygame.image.load('images/background-menu.jpg')

buttons_menu = []
buttons_hiragana = []
buttons_katakana = []
buttons_frases = []
buttons_kanji = []


# draw a button
def draw_button(window, color, message, x1, y1, x2, y2, room):
    pygame.draw.rect(window, color, (x1, y1, x2, y2))
    
    text = FONT_32.render(message, True, WHITE)
    x = x1 + x2/2 - text.get_width()/2
    y = y1 + y2/2 - text.get_height()/2
    window.blit(text, (x, y))

    # Add the buttons info to a list
    room.append([x1, y1, x2, y2, message])
    

# Draws the menu
def draw_menu(window):
    gap = 80
    window.blit(background_menu, (0, 0))
    draw_button(window, BLACK, "Hiragana", (WIDTH/2 - 100), HEIGHT/2 - gap, 200, 40, buttons_menu)
    draw_button(window, BLACK, "Katakana", (WIDTH/2 - 100), HEIGHT/2, 200, 40, buttons_menu)
    draw_button(window, BLACK, "Frases", (WIDTH/2 - 100), HEIGHT/2 + gap, 200, 40, buttons_menu)
    draw_button(window, BLACK, "Kanji", (WIDTH/2 - 100), HEIGHT/2 + gap*2, 200, 40, buttons_menu)


# Checks if a button was pressed and return True and the button pressed or False
def isPressed(button_list, message):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for button in button_list:
        x_check = (mouse_x < button[0] + button[2] and mouse_x > button[0])
        y_check = (mouse_y < button[1] + button[3] and mouse_y > button[1])
        if x_check and y_check:
            # plays sound at click a button
            pygame.mixer.music.load('audios\click_sound.wav')
            pygame.mixer.music.play()

            return button[4]

    return message
