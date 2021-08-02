import pygame
pygame.init()
from menu import *
from character import Character
from variables import *

# sprites 
sprites = {'intruguing_normalRika': pygame.image.load('Rika Sprites/ri_se_de_a1.png'),
            'smiling_normalRika': pygame.image.load('Rika Sprites/ri_se_ni_a1.png'),
            'superSmiling_normalRika': pygame.image.load('Rika Sprites/ri_se_wa_a1.png'),
            'littleSad_normalRika': pygame.image.load('Rika Sprites/ri_se_ko_a1.png')
}

quiz_sprites = {
    False: pygame.image.load('Rika Sprites/ri_se_ko_a1.png'),
    True: pygame.image.load('Rika Sprites/ri_se_wa_a1.png'),
}


class Rika(Character):

    def general(self, window, object, sprites_chosen, buttons, moves, letters, dialogue, restart, sounds):
        # change sprites
        sprite = sprites_chosen.get(object.clicks, 'smiling_normalRika')
        if object.answered:
            sprite_used = quiz_sprites[object.gotItRight]
        else:
            sprite_used = sprites[sprite]

        x = 100
        y = HEIGHT - sprites[sprite].get_height()
            
        draw_button(window, BLACK, "menu", 20, 20, 200, 50, buttons)
        object.draw_character(sprite_used, window, x, y, object.move)
        object.draw_chatbox(window, WIDTH/2 - 300, HEIGHT - 120)
        object.draw_text(window, dialogue, quiz_interactions, quiz_result)
        object.restart_quiz(restart)

        # moves rika
        if object.clicks in list(moves.keys()):
            object.move = object.move_character(moves[object.clicks])
        
        # shows the letters in the screen
        if object.clicks in list(letters.keys()): 
            object.draw_letters(window, letters[object.clicks], sounds, WIDTH/2 + 60, HEIGHT/2)
        
        
        