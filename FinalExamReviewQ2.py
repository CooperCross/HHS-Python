# FinalExamReviewQ2.py
# Cooper Cross
# 1/15/2020

import string, random

print(string.hexdigits)

def is_hex_digit():
    hexdigit = random.choice(string.hexdigits)
    guess = input("Input a Hexdigit: ")
    while guess != hexdigit:
        print("Try again!")
        guess = input("Input a Hexdigit: ")
    print("You guessed the correct hexdigit!")
is_hex_digit()
    
