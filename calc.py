# A simple calculator in python 
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 19th January 2023

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operand = input("Choose one of these (+ - * /): ")

if operand == "+":
  print(first_number + second_number)
elif operand == "-":
  print(first_number - second_number)
elif operand == "*":
  print(first_number * second_number)
elif operand == "/":
  print(first_number / second_number)
else:
  print("Wrong operand choice!")
