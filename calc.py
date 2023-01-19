# A simple calculator in python 
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 19th January 2023

discount = 0.20

unit_price = int(input("Enter the unit price of the product: "))
discounted_price = unit_price * discount 
total_price = unit_price - discounted_price
print(f"Total price is : {total_price}")
