import requests as reqs
import json
from replit import clear
import time

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def get_word():
  return(reqs.get('https://random-word-api.herokuapp.com/word').json())

word = str(get_word())
word = word[2:-2]
hangman_tier = 0
guessed_word = ['_'] * len(word)
wrong_guesses = []
print(word)

def get_guess():
  clear()
  print(hangman[hangman_tier], '\n')
  print(wrong_guesses,'\n')
  print('.'.join(guessed_word), '\n')
  guess = input('Guess a letter: ')
  if len(guess) > 1:
    print('You can only guess a single letter!')
    get_guess()
  else:
    return(guess)
  
  
while ''.join(guessed_word) != word and hangman_tier < 6:
  guess = get_guess()
  if guess in word:
    letter_index = -1
    for i in word:
      letter_index += 1
      if i == guess:
        guessed_word[letter_index] = i
  else:
    print('Letter not in word')
    hangman_tier += 1
    wrong_guesses.append(guess)
    time.sleep(1)
    

clear()
print(hangman[hangman_tier], '\n')
print(wrong_guesses,'\n')
print('.'.join(guessed_word), '\n')

if ''.join(guessed_word) == word:
  print('Congratulations, you won!')
else:
  print('You Lose!')

print('The word is ', word)
