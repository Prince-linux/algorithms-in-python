# A rock, paper, scissors game in python
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 20th January, 2023

import random

item_list = {1: "rock", 2: "paper", 3: "scissors"}

user_win = 0
cpu_win = 0
draw = 0

for counter in range(0, 4):
    if user_win == 2:
        print(f"You are the winner of this game. you won {user_win} games")
        break

    elif cpu_win == 2:
        print(f"You lost {cpu_win} to CPU ")
        break

    elif counter == 3:
      print("The game is a draw")
      break
    try:
      choice = int(input("Type in one of these choices (1:rock, 2:paper, 3:scissors): "))
    except ValueError:
      print("You did not enter a valid number")
      break
    random_choice = random.choice(list(item_list.values()))
    print(f"CPU selection: {random_choice}")
    if item_list[choice] == random_choice:
       print("Draw!")

    if item_list[choice] == "rock":  
        if random_choice == "paper":
            cpu_win += 1
            print("You Lose!")
        elif random_choice == "scissors":
            user_win += 1
            print("You Win!")

    elif item_list[choice] == "paper":
        if random_choice == "rock":
            user_win += 1
            print("You Win!")
      
        elif random_choice == "scissors":
            cpu_win += 1
            print("You Lose!")

    elif item_list[choice] == "scissors":
        if random_choice == "rock":
            cpu_win += 1
            print("You Lose!")
        elif random_choice == "paper":
            user_win += 1
            print("You Win!")