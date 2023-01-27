# A python program that uses for loops to guess a user's input

# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 27th January, 2023

import random

number = random.randrange(0, 3)

for item in range(0, 4):
    guessed_number = int(input("Enter a number from 0 t0 20: "))
    if guessed_number == number:
        print("You guessed right")
        break
    else:
        print("Try again")
else:
    print("Game over! You ran out of chances")

