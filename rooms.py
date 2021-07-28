import pygame
pygame.init()
from rika import *
from variables import *

background_hiragana = pygame.image.load('images/background-hiragana.jpg')
rika_object = Rika()

def add_clicks_hiragana():
    if rika_object.clicks_hiragana in list(hiragana_quiz_letters.keys()) and rika_object.answered == False:
        pass
    else:

        rika_object.clicks_hiragana += 1

    rika_object.answered = False

def hiragana_room(window):
    
    window.blit(background_hiragana, (0, 0))
    rika_object.hiragana(window, rika_object)
    

