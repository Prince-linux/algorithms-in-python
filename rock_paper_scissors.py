# A rock, paper, scissors game in python
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 20th January, 2023

import random

item_list = ["rock", "paper", "scissors"]
choice = input("Type in one of these choices (rock, paper, scissors): ")
rand_choice = random.choice(item_list)

print(f"CPU selection: {rand_choice}")

if choice == "rock":
    if rand_choice == "rock":
        print("Draw!")
    elif rand_choice == "paper":
        print("You Lose!")
    elif rand_choice == "scissors":
        print("You Win!")

elif choice == "paper":
    if rand_choice == "rock":
        print("You Win!")
    elif rand_choice == "paper":
        print("Draw!")
    elif rand_choice == "scissors":
        print("You Lose!")

elif choice == "scissors":
    if rand_choice == "rock":
        print("You Lose!")
    elif rand_choice == "paper":
        print("You Win!")
    elif rand_choice == "scissors":
        print("Draw!")
else:
    print("You made the wrong choice! Game Over!!")

