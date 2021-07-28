import pygame
pygame.init()

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

hiragana_quiz_letters = {13: "あ", 14: "い", 15: "う", 16: "え", 17: "お"}

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
13: "Clique na caixa ao lado para poder digitar sua resposta, eu quero que você escreva o romaji da letra mostrada na tela."

}

quiz_interactions = {
    False: "Ahhh... você errou",
    True: "Yay!!! Você acertou"
}

quiz_sprites = {
    False: 'littleSad_normalRika',
    True: 'superSmiling_normalRika'
}