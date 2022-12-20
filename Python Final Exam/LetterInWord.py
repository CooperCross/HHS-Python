# LetterInWord.py
# Cooper Cross
# 1/22/2020

import string, random

def is_letter_in_word():
    guess = input("Input a word: ")
    
    if randLetter in guess:
        print("")
        print("You got it!")
        print("The correct letter was "+randLetter)
    else:
        print("Try again")
        is_letter_in_word()

is_letter_in_word()
    

