# A python program which prints the user's initials to the screen.
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 18th January 2023

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
first_name = first_name[:1]
last_name = last_name[:1]
print((first_name + last_name).upper())

