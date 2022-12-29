TAX = 0.10 
customer_name = input("Please Enter Customer's name: ")
customer_bill = float(input("Enter Customer's bill: "))
total_tax = customer_bill * TAX 
total_bill = format(customer_bill + total_tax, '.2f') 
print(f"Customer: {customer_name}\nBill: {customer_bill}\nTax: {total_tax}\nTotal: {total_bill}")


