import random
from words import words
import string

def get_valid_word(words):
    chosenword = random.choice(words)
    while '-' in chosenword or ' ' in chosenword:
        chosenword = random.choice(words)
    
    return chosenword.upper()

def hangman():
    chosenword = get_valid_word(words)
    word_letters = set(words)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

user_input = input("Guess a letter: ").upper()
print(user_input)


