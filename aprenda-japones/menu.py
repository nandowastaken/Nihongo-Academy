import pygame
pygame.init()

# images
background_menu = pygame.image.load('images/background-menu.jpg')

# Draws the menu
def draw_menu(window):

    window.blit(background_menu, (0, 0))



    # Updates the skin
    pygame.display.update()
