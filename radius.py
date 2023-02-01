# A radius calculator

# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 1st February, 2023

import math 

def calculate_radius(radius):
    area = round(math.pi*(radius**2), 2)
    return area
    

def get_radius():
    num = int(input("Enter radius: "))
    total_radius = calculate_radius(num)
    return total_radius


def main():
    radius = get_radius()
    print(f"Radius is: {radius}")

main()
