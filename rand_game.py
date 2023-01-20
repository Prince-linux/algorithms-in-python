# A python program that compares user input to a random variable. 
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 20th January, 2023

import random

number = input("Enter any number from 1 to 10: ")
rand_number = random.randint(1, 10) 

if int(number) == rand_number:
  print("You've won")
else:
  print("Try again")
  print(rand_number)

