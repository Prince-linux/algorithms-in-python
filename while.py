# An example of a while loop 
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 31st January 2023

numbers = [10, 99, 100, 98, 85, 45,100, 59, 100, 65, 66, 76, 12, 35, 13, 100, 80, 95]

counter = 0

while counter < len(numbers):
    if numbers[counter] == 100:
        print("found")
    counter += 1 


