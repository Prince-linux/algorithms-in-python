# An example of a while loop.

# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 31st January, 2023

names = ["Prince", "Mark"]

while True: 
    names.append(input("Enter a member's name: "))
    print(names)
    question = ""
    try:
        question = int(input("Do you want to add another name? Press 1 for yes or 2 for no: "))
    except ValueError:
        print(f"You entered a wrong choice: {question}")
        break
        
    if question == 1:
        continue
    elif question == 2:
        break

print(f"These are the names you entered: {names}")


