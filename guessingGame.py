#!/bin/python3
## Guessing Game

def getMean(max, min):
    # function returns mean of two numbers
    return int((max + min)/2)

def processAnswer(answer, max, min, middle, turns):
    #function increments turns taken, then decides how to "home in" on solution 
    turns += 1
    if answer == "H":
        return max, middle, turns
    elif answer == "L": 
        return middle, min, turns
    else:
        return middle, middle, turns

max = 101
min = 0
turns = 0
answer = " "
middle = 0

print("Think of a number between 1 and 100")

while (answer != "S") and (turns < 9):
    middle = getMean(max, min)
    answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
    
    max, min, turns = processAnswer(answer, max, min, middle, turns)
    
if answer != "S":
    print("You tried to fool me! My best guess was {}, and it took {} guesses".format(middle, turns))
else:
    print("Your number is {}, it took me {} guesses".format(middle, turns))
