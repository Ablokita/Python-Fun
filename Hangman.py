import random
import string
from words import english

def valid_word(english):
    word=random.choice(english)
    while '_' in word or ' ' in word:
        word= random.choice(english)

    return word

def hangman():
    word=valid_word(english)
    letters= set(word.upper())  #letters in the word
    alphabet = set(string.ascii_uppercase)   # a set of all the english alphabets in uppercase
    guessed_letters = set()  #set of letters guessed by the user
    lives = 10


    while len(letters) > 0 and lives > 0:
        print('You have ', lives,'lives left and the letters you have already used are : ', ' '.join(guessed_letters))
        word_list= [char if char in guessed_letters else '-' for char in word]
        print('Current Word : ', ' '.join(word_list))

        user_letter = input('Guess a letter ').upper()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
            else:
                lives = lives-1
                print('Letter not in word ')

        elif user_letter in letters:
            print('You have already used the characters !  Please try a different character ')
        else:
            print('Invalid Input !!')

    if lives == 0:
        print('You died sorry :( \n The word was ', word)
    else:
        print('Yay !! You guessed the word ', word,' !! :) ')


hangman()