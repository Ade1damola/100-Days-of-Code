# SHOPPING BILL WITH DISCOUNT
price = float(input("Enter product price: "))
quantity = float(input("Enter quantity of products: "))
amount = price * quantity
discount= float(input("Enter discount for product: "))
discounted_price = (discount * amount) / 100 + amount

print("Amount: ", amount)
print("Discount:", discount, "%")
print("Discounted Price:", discounted_price)