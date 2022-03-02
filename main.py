import pygame
pygame.init()
from menu import *
from variables import WIDTH, HEIGHT
from rooms import *
from quiz import *
from useful_functions import translateAlphabet
from character import Character

# screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nihongo Academy')
pygame.display.set_icon(icon)

# Run the game
def main():
    clock = pygame.time.Clock()
    running = True
    change_room = "menu"

    # different quizzes
    quiz_hiragana = Quiz(screen, hiragana_quiz_letters)
    quiz_katakana = Quiz(screen, katakana_quiz_letters)
    quiz_frases = Quiz(screen, frases_quiz)
    quiz_kanji = Quiz(screen, kanji_letters)

    # quiz vars
    clicks_hiragana = 1
    clicks_katakana = 1
    clicks_frases = 1
    clicks_kanji = 1

    clicks = clicks_hiragana

    object_used = rika_hiragana
    object_quiz_box_active = quiz_hiragana
    boxes_scenes = draw_box_hiragana

    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_room == "menu":
                    change_room = isPressed(buttons_menu, 'menu')
                elif change_room == "Hiragana":
                    
                    change_room = isPressed(buttons_hiragana, 'Hiragana')
                    object_used = rika_hiragana
                    object_quiz_box_active = quiz_hiragana
                    boxes_scenes = draw_box_hiragana
                    clicks = clicks_hiragana
                    manage_clicks(rika_hiragana, quiz_hiragana, give_results_hiragana, hiragana_quiz_letters, 'Hiragana', change_room, clicks_hiragana)

                elif change_room == "Katakana":
                    change_room = isPressed(buttons_katakana, "Katakana")
                    object_used = rika_katakana
                    object_quiz_box_active = quiz_katakana
                    boxes_scenes = draw_box_katakana
                    clicks = clicks_katakana
                    manage_clicks(rika_katakana, quiz_katakana, give_results_katakana, katakana_quiz_letters, 'Katakana', change_room, clicks_katakana)

                elif change_room == "Frases":
                    change_room = isPressed(buttons_frases, "Frases")
                    object_used = rika_frases
                    object_quiz_box_active = quiz_frases
                    boxes_scenes = draw_box_frases
                    clicks = clicks_frases
                    manage_clicks(rika_frases, quiz_frases, give_results_frases, frases_quiz, 'Frases', change_room, clicks_frases)
                elif change_room == "Kanji":
                    change_room = isPressed(buttons_kanji, "Kanji")
                    object_used = rika_kanji
                    object_quiz_box_active = quiz_kanji
                    boxes_scenes = draw_box_kanji
                    clicks = clicks_kanji
                    manage_clicks(rika_kanji, quiz_kanji, give_results_kanji, kanji_letters, 'Kanji', change_room, clicks_kanji)

                # checks if the box is active or not
                if object_quiz_box_active.input_rect.collidepoint(event.pos) and object_quiz_box_active.answered == False and object_used.clicks in boxes_scenes:
                    object_quiz_box_active.active = True
                    clicks = -1
                    continue
                elif object_used.clicks in boxes_scenes:
                    object_quiz_box_active.active = False
                    clicks += 1
                else:
                    object_quiz_box_active.active = False
                    clicks += 2
            # writes user's input in screen
            if event.type == pygame.KEYDOWN:
                if change_room == "Hiragana":
                    manage_quiz(event, rika_hiragana, quiz_hiragana, translateAlphabet, hiragana, clicks_hiragana)
                elif change_room == "Katakana":                  
                    manage_quiz(event, rika_katakana, quiz_katakana, translateAlphabet, katakana, clicks_katakana)

                if event.key == pygame.K_LEFT:
                    go_back(object_used, boxes_scenes, change_room)
            
        # chooses which scenary to draw
        if change_room == "menu":
            draw_menu(screen)
            
        elif change_room == "Hiragana":
            hiragana_room(screen)
            draw_questions_quiz(quiz_hiragana, rika_hiragana, hiragana_quiz_letters, draw_box_hiragana)

        elif change_room == "Katakana":
            katakana_room(screen)
            draw_questions_quiz(quiz_katakana, rika_katakana, katakana_quiz_letters, draw_box_katakana)

        elif change_room == "Frases":
            frases_room(screen)

        elif change_room == "Kanji":
            kanji_room(screen)

        
        pygame.display.update()
        

main()
