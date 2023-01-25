# A rock, paper, scissors game in python
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 20th January, 2023

import random

item_list = {1: "rock", 2: "paper", 3: "scissors"}
choice = int(input("Type in one of these choices (1:rock, 2:paper, 3:scissors): "))
random_choice = random.choice(list(item_list.values()))

print(f"CPU selection: {random_choice}")

if item_list[choice] == "rock":
    if random_choice == "rock":
        print("Draw!")
    elif random_choice == "paper":
        print("You Lose!")
    elif random_choice == "scissors":
        print("You Win!")

elif item_list[choice] == "paper":
    if random_choice == "rock":
        print("You Win!")
    elif random_choice == "paper":
        print("Draw!")
    elif random_choice == "scissors":
        print("You Lose!")

elif item_list[choice] == "scissors":
    if random_choice == "rock":
        print("You Lose!")
    elif random_choice == "paper":
        print("You Win!")
    elif random_choice == "scissors":
        print("Draw!")
else:
    print("You made the wrong choice! Game Over!!")

