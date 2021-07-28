import pygame
pygame.init()
from character import Character
from variables import *

# sprites 
sprites = {'intruguing_normalRika': pygame.image.load('Rika Sprites/ri_se_de_a1.png'),
            'smiling_normalRika': pygame.image.load('Rika Sprites/ri_se_ni_a1.png'),
            'superSmiling_normalRika': pygame.image.load('Rika Sprites/ri_se_wa_a1.png'),
            'littleSad_normalRika': pygame.image.load('Rika Sprites/ri_se_ko_a1.png')
}

# sprites used in scenes
sprite_choice = {0: 'smiling_normalRika', 1: 'superSmiling_normalRika', 2: 'intruguing_normalRika', 
3: 'superSmiling_normalRika', 4: 'smiling_normalRika', 5: 'smiling_normalRika', 6: 'superSmiling_normalRika', 
12: 'superSmiling_normalRika'
}

quiz_sprites = {
    False: pygame.image.load('Rika Sprites/ri_se_ko_a1.png'),
    True: pygame.image.load('Rika Sprites/ri_se_wa_a1.png'),
}

hiragana_letters = {7: "あ", 8: "い", 9: "う", 10: "え", 11: "お"}


# movements
moves_hiragana = {7: (0, HEIGHT - 120), 12: (100, HEIGHT - 120), 13: (0, HEIGHT - 120)}


class Rika(Character):
    def draw_letters(self, window, letter, audio, x, y):
    
        text = BIG_FONT_TEXT.render(letter, True, WHITE)
        window.blit(text, (x, y))

    def hiragana(self, window, object_rika):
        # change sprites
        sprite = sprite_choice.get(self.clicks_hiragana, 'smiling_normalRika')
        if self.answered:
            sprite_used = quiz_sprites[self.gotItRight]
        else:
            sprite_used = sprites[sprite]

        x = 100
        y = HEIGHT - sprites[sprite].get_height()
        
        object_rika.draw_character(sprite_used, window, x, y, self.move)
        object_rika.draw_chatbox(window, WIDTH/2 - 300, HEIGHT - 120)
        object_rika.draw_text(window, dialogue_hiragana, quiz_interactions, self.clicks_hiragana)

        # moves rika
        if self.clicks_hiragana in list(moves_hiragana.keys()):
            self.move = object_rika.move_character(moves_hiragana[self.clicks_hiragana])
    
        # shows the letters in the screen
        if self.clicks_hiragana in list(hiragana_letters.keys()): 
            object_rika.draw_letters(window, hiragana_letters[self.clicks_hiragana], '', WIDTH/2 + 60, HEIGHT/2)
    
        