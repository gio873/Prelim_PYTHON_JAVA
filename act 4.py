item1 = float(input("Enter the cost of the first item: "))
item2 = float(input("Enter the cost of the second item: "))
payment = float(input("Enter your payment amount: "))

total_cost = item1 + item2

if payment < total_cost:
    owed = total_cost - payment
    print(f"Invalid payment. You still owe ${owed:.2f}")
else:
    change = payment - total_cost
    print(f"Thank you for your payment! Your change is ${change:.2f}")
