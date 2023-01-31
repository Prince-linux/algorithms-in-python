# An example of a while loop use case in a dice game

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 31st January, 2023

import random 

while True:
    user_input = int(input("Press 1.Roll Dice 2.Exit Game: "))
    if user_input == 1:
        rand = random.randint(1, 6)
        print(rand)
    else:
        break

