import pygame
pygame.init()
from menu import *
from variables import WIDTH, HEIGHT
from rooms import *
from quiz import *
from character import Character

# screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Aprenda Japonês')

# Run the game
def main():
    clock = pygame.time.Clock()
    running = True
    change_room = "menu"

    # quiz vars
    quiz_text = Quiz(screen, hiragana_quiz_letters)
    count_clicks = 1

    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_room == "menu":
                    change_room = isPressed()
                    continue
                
                # checks if the box is active or not
                if quiz_text.input_rect.collidepoint(event.pos):
                    quiz_text.active = True
                    count_clicks = -1
                    continue
                else:
                    quiz_text.active = False
                    count_clicks += 1

                if change_room == "Hiragana" and quiz_text.active == False and count_clicks != 0:
                    add_clicks_hiragana()
                    # starts quiz
                    if rika_object.clicks_hiragana in hiragana_quiz_letters:
                        quiz_text.remove = True

                
            # writes user's input in screen
            if event.type == pygame.KEYDOWN:
                if quiz_text.active:
                    # enters the answer
                    if event.key == pygame.K_RETURN:
                        rika_object.answered = True
                        rika_object.gotItRight = quiz_text.answer_result_quiz()

                        quiz_text.user_text = ''
                        quiz_text.active = False
                        count_clicks += 1

                    elif event.key == pygame.K_BACKSPACE:
                        quiz_text.user_text = quiz_text.user_text[:-1]
                    else:
                        quiz_text.user_text += event.unicode
                    
        
        if change_room == "menu":
            draw_menu(screen)
        elif change_room == "Hiragana":
            hiragana_room(screen)

            # draw questions of the quiz
            if rika_object.clicks_hiragana in hiragana_quiz_letters:
                quiz_text.draw_questions(WIDTH/2 + 60, HEIGHT/2 - 30)
            


        quiz_text.render_text()
        pygame.display.update()
        

main()
