# A python program that prints match was found if user's input is in the list
# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 18th January 2023

names = ["Prince", "Andre", "Doris", "Zoey", "Fobi", "Gyamfi", "Osei", "Felicia", "Paulina", "Jones", "Azada", "Mawuli", "Emma", "Agbesi"]

search_name = input("Enter a name: ")

try:
  names.index(search_name)
except ValueError: 
  print("No match found!")
else:
  print("Match found!")