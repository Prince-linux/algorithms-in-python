# A bill calculator where a 10% ddiscount is applied.

# Author: Prince Oppong Boamah<regioths@gmail.com>
# Date: 1st February, 2023.

def calculate_discount(total):
    discount = total - total / 100 * 10
    return discount

def get_total():
    bill = int(input("Enter total: "))
    bill_total = format(calculate_discount(bill), '.2f')
    return bill_total

def main():
    total = get_total()
    print(f"Your bill is: ${total}")

main()


