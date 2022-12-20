# Contestant 00060151

import random

# Returns input of the number of lock combos to display
def get_how_many_to_list():
    return int(input("Enter number of lock combinations to display: "))

# Returns a random number between two integers, min and max (inclusive)
def get_number(min, max):
    return random.randrange(min, max)

# Returns a formatted string of the combo numbers
def next_combo_number(numbers):
    string = ""
    for i in range(numbers):
        string += str(get_number(0,9))
        string += " "

    return string

# Prompts the user for number of digits in combo, gives an error if the
# number is too small, and re-initiates the function
def get_number_in_dials():
    number = int(input("Enter number of dials: "))
    if number < 3:
        print("The number of dials must be at least 3\n")
        get_number_in_dials()
    return number
    
number_dials = get_number_in_dials()
number_combos = get_how_many_to_list()

# Uses the functions from above to produce the desired output from the input
for i in range(number_combos):
    print("Number " + str(i) + ": " + str(next_combo_number(number_dials)))
print("Generated " + str(number_combos) + " combos")
