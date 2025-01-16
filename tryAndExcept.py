#try and except method will not crash the code rather it will let you run again

import random

numberToGuess = random.randint(1,100)

try:
    userInput = int(input("enter any number to guess: "))
except:
    print("Try Again!!")


