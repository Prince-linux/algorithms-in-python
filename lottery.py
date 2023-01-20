# A lottery program in python 
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 20th January, 2023

import random 

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90]
lottery_numbers = random.sample(numbers, 6)
print("The following are the lottery numbers")
print(*lottery_numbers)


