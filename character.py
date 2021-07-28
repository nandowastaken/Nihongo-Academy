import pygame
import time
pygame.init()
from variables import *
from useful_functions import operatorSign

class Character:
    
    def __init__(self):
        self.clicks_hiragana = 0

        # text variables
        self.x_text, self.y_text = WIDTH/2 - 300, HEIGHT - 120

        # movement variables
        self.move = [False]
        self.x_destination, self.y_destination = 100, 0

        # quiz variables
        self.answered = False
        self.gotItRight = False
    
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
    
    def draw_text(self, window, message, message_quiz, clicks):
        # determines what Rika will say
        if self.answered:
            words = message_quiz[self.gotItRight].split()

        elif clicks < len(message) and self.answered == False:
            words = message[clicks].split()
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




