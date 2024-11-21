cost_price = float(input("Enter cost price: "))
sales_price = float(input("Enter sales price: "))

if sales_price > cost_price:
    print("Profit is $", sales_price - cost_price)
elif cost_price > sales_price:
    print("Loss is $", cost_price - sales_price)
else:
    print("There is no profit or loss")