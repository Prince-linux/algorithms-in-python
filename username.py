# An example of a use case of functions in python 

# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 1st February, 2023

def return_username():
    username = input("Enter username: ")
    return username

def main():
    name = return_username()
    print(name)


main()
