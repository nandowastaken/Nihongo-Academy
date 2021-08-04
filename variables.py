import pygame
pygame.init()

# screen icon
icon = pygame.image.load('images/icon.jpg')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color_active = pygame.Color('lightskyblue3')
color_passive = WHITE
FPS = 60
WIDTH, HEIGHT = (800, 500)

# a gap between each word that is printed in the screen
GAP_WORD = 14

# fonts
FONT_32 = pygame.font.Font("Higurashi_Fonts\ReishoE1-Regular\ReishoE1-Regular.ttf", 48)
FONT_TEXT = pygame.font.Font('fonts\GenEiKoburiMin_v6.1\GenEiKoburiMin6-R.ttf', 22)
BIG_FONT_TEXT = pygame.font.Font('fonts\GenEiKoburiMin_v6.1\GenEiKoburiMin6-R.ttf', 70)

# alphabets
hiragana = {'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o'}
katakana = {'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o'}

# sprites
sprites = {'intruguing_normalRika': pygame.image.load('Rika Sprites/ri_se_de_a1.png'),
            'smiling_normalRika': pygame.image.load('Rika Sprites/ri_se_ni_a1.png'),
            'superSmiling_normalRika': pygame.image.load('Rika Sprites/ri_se_wa_a1.png'),
            'littleSad_normalRika': pygame.image.load('Rika Sprites/ri_se_ko_a1.png')
}

# sprites used in scenes
sprite_choice_hiragana = {0: 'smiling_normalRika', 1: 'superSmiling_normalRika', 2: 'intruguing_normalRika', 
3: 'superSmiling_normalRika', 4: 'smiling_normalRika', 5: 'smiling_normalRika', 6: 'superSmiling_normalRika', 
12: 'superSmiling_normalRika'
}

sprite_choice_katakana = {0: 'superSmiling_normalRika', 1: 'intruguing_normalRika', 2: 'superSmiling_normalRika'}

sprite_choice_frases = {0: 'superSmiling_normalRika', 3: 'intruguing_normalRika', 4: 'superSmiling_normalRika'}

sprite_choice_kanji = {0: 'superSmiling_normalRika'}

quiz_sprites = {
    False: pygame.image.load('Rika Sprites/ri_se_ko_a1.png'),
    True: pygame.image.load('Rika Sprites/ri_se_wa_a1.png'),
}

# sounds

hiragana_sounds = {
    7: 'audios/a.mp3',
    8: 'audios/i.mp3',
    9: 'audios/u.mp3',
    10: 'audios/e.mp3',
    11: 'audios/o.mp3'
}

katakana_sounds = {
    6: 'audios/a.mp3',
    7: 'audios/i.mp3',
    8: 'audios/u.mp3',
    9: 'audios/e.mp3',
    10: 'audios/o.mp3'
}

frases_sounds = {}

kanji_sounds = {}

# letters
hiragana_letters = {7: "あ", 8: "い", 9: "う", 10: "え", 11: "お"}
katakana_letters = {6: "ア", 7: "イ", 8: "ウ", 9: "エ", 10: "オ"}
frases = {}
kanji_letters = {}

# quiz results list
give_results_hiragana = [18]
give_results_katakana = [17]
give_results_frases = []
give_results_kanji = []

restart_quiz_hiragana = {19: 13}
restart_quiz_katakana = {18: 12}
restart_quiz_frases = {}
restart_quiz_kanji = {}

# movements
moves_hiragana = {
    6: (WIDTH/2 - 300, HEIGHT - 120), 7: (0, HEIGHT - 120), 11: (0, HEIGHT - 120), 
    12: (100, HEIGHT - 120), 13: (0, HEIGHT - 120)

}
moves_katakana = {
    5: (WIDTH/2 - 300, HEIGHT - 120), 6: (0, HEIGHT - 120), 10: (0, HEIGHT - 120), 11: (100, HEIGHT - 120), 
    12: (0, HEIGHT - 120)

}
moves_frases = {}
moves_kanji = {}


# backgrounds
background_hiragana = pygame.image.load('images/background_hiragana.jpg')
background_katakana = pygame.image.load('images/background_katakana.jpg')
background_frases = pygame.image.load('images/background_frases.jpg')
background_kanji = pygame.image.load('images/background_kanji.jpg')

# quizzes 
hiragana_quiz_letters = {13: "あ", 14: "い", 15: "う", 16: "え", 17: "お"}
katakana_quiz_letters = {12: "ア", 13: "イ", 14: "ウ", 15: "エ", 16: "オ"}
frases_quiz = {}
kanji_quiz_letters = {}

# when draw box of the quizzes
draw_box_hiragana = [13, 14, 15, 16, 17]
draw_box_katakana = [12, 13, 14, 15, 16]
draw_box_frases = []
draw_box_kanji = []

# dialogues
dialogue_hiragana = {0: "こにちは！Esta é a primeira vez que nos encontramos, não é? Meu nome é Rika Furude, prazer em conhecê-lo!"

,
1: "Esta seção é dedicada a aprender o Hiragana!!!", 2: "hum.... você não sabe o que é o hiragana?", 
3: "Bem, não tem problema, é apenas normal que você não saiba o que é, afinal é sua primeira aula!",
4: "Hiragana é um alfabeto fonético, isso significa que são um conjunto de símbolos que representam um som.",
5: "Por exemplo, a letra あ representa o som 'a', a letra い representa o som 'i', a letra え representa o som 'e', a letra う representa o som 'u', e a letra お representa o som 'o'.", 
6: "Escrever palavras em Japonês usando o alfabeto latino, como eu fiz agora, é chamado de Romaji! Agora, vamos dar uma ouvida nesses sons!", 
7: "a", 8: "i", 9: "u", 10: "e", 11: "o",
12: "Agora que você deu uma olhada nos sons e na escrita, vamos fazer um quiz, ok?", 
13: "Clique na caixa ao lado para poder digitar sua resposta, eu quero que você escreva o romaji da letra mostrada na tela.", 
19: "Vamos prosseguir com o seu aprendizado"

}

dialogue_katakana = {
    0: "Bem-vindo à seção de Katakana.",
    1: "hum... você não sabe o que é o katakana?",
    2: "Bem, não tem problema! É para isso que você está aqui, não é? Para aprender!",
    3: "Katakana, assim como o Hiragana, é um alfabeto fonético, ele também representa sons. É muito utilizado para representar nomes de coisas ou pessoas estrangeiras!",
    4: "Vejamos estas letras: A letra ア representa o som 'a', a letra イ representa o som 'i', a letra ウ representa o som 'u', a letra エ representa o som 'e', a letra オ representa a letra 'o'.",
    5: "Como eu disse na seção de Hiragana, representar os sons/letras japonesas chama-se Romaji!",
    6: "a", 7: "i", 8: "u", 9: "e", 10: "o",
    11: "Agora que você deu uma olhada nos sons e na escrita, vamos fazer um quiz, ok?"
}

dialogue_frases = {
    0: "Bem-vindo à seção de frases! Aqui você vai usar os alfabetos que você aprendeu nas últimas duas seções para formar frases básicas.",
    1: "Vamos começar com afirmações básicas em Japonês. Elas seguem uma estrutura simples: X は Y です, por exemplo: わたしはりかです",
    2: "X é um tópico, は marca este tópico, é uma partícula que indica que algo é o tópico da sentença.",
    3: "hum... não sabe o que é uma partícula?",
    4: "Certo! Uma partícula é uma palavra como は que geralmente marcam algo que vem antes delas, estas partículas descrevem algo sobre este objeto X que vem antes.",
    5: "Como foi dito antes, a partícula は marca o tópico da sentença, nesse caso, o tópico da sentença é わたし, que é o X, isso significa 'Eu', é a forma mais comum de se dizer 'Eu' em Japonês.",
    6: "Y é algo sobre X, o que X é",
    7: "です é como se afirma algo na senteça, é uma confirmação, traduzindo a frase わたしはりかです, significa 'Eu sou Rika', ou 'Meu nome é Rika'."
}

dialogue_kanji = {
    0: "Bem-vindo à seção de Kanji!",
    1: "Kanji também é um alfabeto japonês, só que escrito, ao invés de fonético, isso significa que os símbolos representam significados.",
    2: "Vamos pegar o kanji 私, ele significa 'Eu', para se ler kanji, utiliza-se do hiragana ou do katakana, nesse caso, o kanji 私 ler-se わたし",
    3: "Os kanjis são utilizados em frases ao invés de se escrever tudo em Katakana ou Hiragana, por exemplo:　私ははりかです, se você frequentou a seção de frases, você sabe que isso significa 'Meu nome é Rika'"
}


quiz_interactions = {
    False: "Ahhh... você errou",
    True: "Yay!!! Você acertou"
}

quiz_sprites = {
    False: 'littleSad_normalRika',
    True: 'superSmiling_normalRika'
}

quiz_result = {
    False: "Eu acho que você ainda deve praticar um pouco mais...!",
    True: "Parabéns! Você acertou todas as questões, você definitivamente aprendeu este assunto!"
}