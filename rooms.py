import pygame
pygame.init()
from rika import *
from variables import *

rika_hiragana = Rika()
rika_katakana = Rika()
rika_frases = Rika()
rika_kanji = Rika()

def go_back(object, quiz_questions, room):
    if object.clicks not in quiz_questions and room != "menu" and object.clicks > 0 and (object.clicks - 2) not in quiz_questions:
        object.clicks -= 1

def add_clicks(object, letters):
    if object.clicks in list(letters.keys()) and object.answered == False:
        pass
    else:   
        object.clicks += 1

    object.completed = False
    object.answered = False
    object.played = False

def manage_clicks(object, quiz_object, results, letters, room_checked, room, clicks):
    if room_checked == room and quiz_object.active == False and clicks != 0:
        add_clicks(object, letters)

        # draws questions
        if object.clicks in letters and quiz_object.answered:
            quiz_object.remove = True

        # checks if its the time to announce a result of the quiz
        if object.clicks in results:
            object.completed, object.passed = quiz_object.passed_quiz()

def draw_questions_quiz(quiz, object, letters, box_scenes):
    # draw questions of the quiz
    if object.clicks in letters:
        quiz.draw_questions(WIDTH/2 + 60, HEIGHT/2 - 30)
            
    quiz.render_text(object, box_scenes)

# takes users answers and check if they are right
def manage_quiz(event, object, quiz, translate, alphabet, clicks):
    if quiz.active:
        if event.key == pygame.K_RETURN:
            object.answered = True
            object.gotItRight = quiz.answer_result_quiz(translate, alphabet)
            quiz.user_text = ''
            quiz.answered = True
            quiz.active = False
            clicks += 2

        elif event.key == pygame.K_BACKSPACE:
            quiz.user_text = quiz.user_text[:-1]
        else:
            quiz.user_text += event.unicode

def hiragana_room(window):
    window.blit(background_hiragana, (0, 0))
    rika_hiragana.general(window, rika_hiragana, sprite_choice_hiragana, buttons_hiragana, moves_hiragana, hiragana_letters, dialogue_hiragana, restart_quiz_hiragana, hiragana_sounds)

def katakana_room(window):
    window.blit(background_katakana, (0, 0))
    rika_katakana.general(window, rika_katakana, sprite_choice_katakana, buttons_katakana, moves_katakana, katakana_letters, dialogue_katakana, restart_quiz_katakana, katakana_sounds)

def frases_room(window):
    window.blit(background_frases, (0, 0))
    rika_frases.general(window, rika_frases, sprite_choice_frases, buttons_frases, moves_frases, frases, dialogue_frases, restart_quiz_frases, frases_sounds)

def kanji_room(window):
    window.blit(background_kanji, (0, 0))
    rika_kanji.general(window, rika_kanji, sprite_choice_kanji, buttons_kanji, moves_kanji, kanji_letters, dialogue_kanji, restart_quiz_kanji, kanji_sounds)


