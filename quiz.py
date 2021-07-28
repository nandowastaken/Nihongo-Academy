import pygame
import random
from useful_functions import translateHiragana
from variables import *
from rooms import rika_object
pygame.init()

draw_box_scenes = [13, 14, 15, 16, 17]


class Quiz:
    def __init__(self, window, letters):
        self.window = window

        # quiz type box variables
        self.user_text = ''
        self.draw = False
        self.active = False
        self.color = color_passive
        self.input_rect = pygame.Rect(450, 300, 140, 32)

        # quiz in game variables
        self.answered = False
        self.letters_scenes = letters
        self.letters = list(letters.values())
        self.remove = True
        self.count_answers = 0

        self.resultAnswer = 0
        self.letter = ''
        self.answer = ''
    
    def draw_questions(self, x, y):
        # chose a random letter from the quiz 
        if self.remove and (self.answered == True or self.count_answers == 0):
            self.letter = random.choice(self.letters)
            self.letters.remove(self.letter)
            self.remove = False
            self.count_answers += 1

        text = BIG_FONT_TEXT.render(self.letter, True, WHITE)
        self.window.blit(text, (x, y))
    
    
    def render_text(self):
        # checks if its a scene to draw a box
        if rika_object.clicks_hiragana in draw_box_scenes:
            self.draw = True
        else:
            self.draw = False
        
        if self.draw:
            if self.active:
                self.color = color_active
            else:
                self.color = color_passive

            pygame.draw.rect(self.window, self.color, self.input_rect, 2)

            text = FONT_TEXT.render(self.user_text, True, WHITE)
            self.window.blit(text, (self.input_rect.x + 5, self.input_rect.y + 5))

            self.input_rect.w = max(100, text.get_width() + 10)

    def answer_result_quiz(self):
        self.answer = self.user_text

        if self.answer == translateHiragana(self.letter):
            return True
        else:
            return False
        