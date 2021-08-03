import pygame
import random
from variables import *
pygame.init()

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
        self.phase = 1
        self.answered = False
        self.letters_scenes = letters
        self.letters = list(self.letters_scenes.values())[:self.phase * 5]
        self.remove = True
        self.count_answers = 0

        # correct answers
        self.mastery = 0
        self.letter = ''
        self.answer = ''
        self.completed = False
        self.passed = False
    
    def draw_questions(self, x, y):
        # chose a random letter from the quiz 
        if self.letters == []:
            self.phase += 1
            
        if self.remove and (self.answered == True or self.count_answers == 0):
            self.letter = random.choice(self.letters)
            self.letters.remove(self.letter)
            self.remove = False
            self.answered = False
            self.count_answers += 1

        text = BIG_FONT_TEXT.render(self.letter, True, WHITE)
        self.window.blit(text, (x, y))
    
    
    def render_text(self, object, when_draw_box):
        # checks if its a scene to draw a box
        if object.clicks in when_draw_box:
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

    def answer_result_quiz(self, translation, alphabet):
        self.answer = self.user_text.lower()
        if self.answer == translation(self.letter, alphabet):
            self.mastery += 1
            return True
        else:
            return False
    
    def passed_quiz(self):
        self.completed = True
        
        if self.mastery == 5:
            self.passed = True
        else:
            self.passed = False
            self.phase -= 1

        # reset game
        self.active = False
        self.letter = ''
        self.count_answers = 0
        self.remove = True
        self.answered = False
        self.mastery = 0
        self.letters = list(self.letters_scenes.values())[:self.phase * 5]

        return [self.completed, self.passed]
        