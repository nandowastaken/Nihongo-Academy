<p align="center">
  <img src="https://i.imgur.com/hO0BuIf.png" alt="Game intro scene. Rika is introducing herself">
</p>

# Nihongo Academy

Nihongo Academy is a visual light novel game inspired in Higurashi When They Cry, that's why it uses the game scenarios and characters. In Nihongo Academy, the focus is to learn Japanese, and your teacher, Rika Furude, will teach you, she will explain japanese concepts and words to you and then test your knowledge through a quiz, which you only pass after nailing every question!

If you are interested in see what specifically the game does, check the **Gameplay** section of this Readme. If you want to know how the game was coded, which might help you in a project of yours, or even if you just want to play around with my code, check the **Code** section. 

<h3 align="center"> Gameplay</h3>

<p align="center"> 
  <img src="https://i.imgur.com/450OEJY.png">
</p>

When you start playing, the first thing that appears is a menu with 4 buttons (see image above), each button redirects to a room that specifically teachs you a subject of the japanese language. 

The game has a pretty simple gameplay, Rika will teach you something about Japanese, after you read what she has told you, you click on the screen and she will say something else. When she finished talking, there will be a quiz where you test your knowledge. In case you missed something she said, you can come back by pressing the left arrow in your keyboard.

<h3 align="center">Quiz</h3>

<p align="center">
  <img src="https://i.imgur.com/lrkX8A6.png">
</p>

To answer the quiz, you must click inside that white box and write your answer. Of course that the answer was already "given" to you, since she just explained that, but, trust me, you will still get it wrong at first try (unless you have a really good memory or already had contact with Japanese before). 

### Code 

Overall, there is a lot of lines responsible for different functionalities of the game, the name of the files are pretty self-explanatory, however, there is something that is very interesting for you to know: This game is completely based in python dictionaries. As you already know, the gameplay consists of clicks, you click to pass a dialogue, and the game continues, so the code of this game counts the amount of clicks you gave so that he knows in which part of the game he is. Let's see an example, the image below is a dictionary responsible for the dialogue in the Hiragana section:

~~~python
dialogue_hiragana = {0: "???????????????Esta ?? a primeira vez que nos encontramos, n??o ??? Meu nome ?? Rika Furude, prazer em conhec??-lo!",
1: "Esta se????o ?? dedicada a aprender o Hiragana!!!", 2: "hum.... voc?? n??o sabe o que ?? o hiragana?", 
3: "Bem, n??o tem problema, ?? apenas normal que voc?? n??o saiba o que ??, afinal ?? sua primeira aula!",
4: "Hiragana ?? um alfabeto fon??tico, isso significa que s??o um conjunto de s??mbolos que representam um som.",
5: "Por exemplo, a letra ??? representa o som 'a', a letra ??? representa o som 'i', a letra ??? representa o som 'e', a letra ??? representa o som 'u', e a letra ??? representa o som 'o'.", 
6: "Escrever palavras em Japon??s usando o alfabeto latino, como eu fiz agora, ?? chamado de Romaji! Agora, vamos dar uma ouvida nesses sons!", 
7: "a", 8: "i", 9: "u", 10: "e", 11: "o",
12: "Agora que voc?? deu uma olhada nos sons e na escrita, vamos fazer um quiz, ok?", 
13: "Clique na caixa ao lado para poder digitar sua resposta, eu quero que voc?? escreva o romaji da letra mostrada na tela.", 
19: "Vamos prosseguir com o seu aprendizado"
}
~~~

The number in the left is the amount of clicks you gave, and the text is something that Rika will say at that exactly same moment. So, basically, if you want to continue to add content to this game, you just need to put new things at these dictionaries, as much as you wish. You can continue and make a giant game without writing a single like of code at all! And that is the most important part of the code in this game.

### How can I use this code?

Use it as you wish, the only thing you cannot do is copying this and claiming to be yours, that would be fraud, and fraud isn't very nice, is it? However, if you want to study it, do it, if you want to make this code better, do it, you can even replace all the images and text to make a completely different game, using this code as a skeleton. Do whatever you want, and if you do something really cool, let me know, I'd love to see that. Here's my contact information:

<br>

<p align="center">
  
  <a href="https://www.instagram.com/nandowastaken/">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank" alt="My instagram">
  </a>
  
  <a href="https://twitter.com/nandowastaken">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" target="_blank" alt "My Twitter">
  </a>
  
</p>
