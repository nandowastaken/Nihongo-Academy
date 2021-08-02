import pygame
pygame.init()
from variables import *
from pygame import mixer
from useful_functions import operatorSign, mastery_classification

class Character:
    
    def __init__(self):
        self.clicks = 0
        self.answer_count = 0
        self.mastery_hiragana = 0

        # text variables
        self.x_text, self.y_text = WIDTH/2 - 300, HEIGHT - 120

        # audio variables
        self.played = False

        # movement variables
        self.move = [False]
        self.x_destination, self.y_destination = 100, 0

        # quiz variables
        self.answered = False
        self.gotItRight = False

        self.completed = False
        self.passed = False
    
    def draw_letters(self, window, letter, audio, x, y):
        text = BIG_FONT_TEXT.render(letter, True, WHITE)
        window.blit(text, (x, y))

        if self.played == False:
            pygame.mixer.music.load(audio.get(self.clicks, 'audios/a.mp3'))
            pygame.mixer.music.play()
            self.played = True
    
    def move_character(self, coordinates):
        return [True, coordinates[0], coordinates[1]]

    def draw_character(self, sprite, window, x, y, movement):
        # moves the character
        speed = 10
        if movement[0]:
            distance_x = self.x_destination - movement[1] 
            if self.x_destination != movement[1]:
                self.x_destination += (speed * operatorSign(distance_x)) * -1
            window.blit(sprite, (self.x_destination, y))
            
        else:
            window.blit(sprite, (x, y))
        

    def draw_chatbox(self, window, x1, y1):
        self.x1 = x1
        self.y1 = y1
        pygame.draw.rect(window, BLACK, (x1, y1, 600, 120))
    
    def draw_text(self, window, message, message_quiz, message_results):
        # determines what Rika will say
        if self.answered:
            words = message_quiz[self.gotItRight].split()
        elif self.completed:
            words = message_results[self.passed].split()        
        elif self.clicks in list(message.keys()) and self.answered == False:
            words = message.get(self.clicks, '').split()
        else:
            words = ''

        for word in words:
            text = FONT_TEXT.render(word, True, WHITE)

            # checks if a line has been finished
            if self.x_text + text.get_width() > 700:
                self.x_text = self.x1
                self.y_text += 20

            window.blit(text, (self.x_text, self.y_text))

            # adds the gap between the word
            self.x_text += text.get_width() + GAP_WORD

            
        self.x_text = self.x1
        self.y_text = self.y1

    def restart_quiz(self, scenes):
        if self.clicks in list(scenes.keys()) and self.passed == False:
            self.clicks = scenes[self.clicks]




