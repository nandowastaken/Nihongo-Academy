import pygame
pygame.init()
from menu import draw_menu

# colors
BLACK = (255, 255, 255)

# screen settings
WIDTH, HEIGHT = (800, 500)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Aprenda Japonês')

# Run the game
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_menu(screen)

main()
