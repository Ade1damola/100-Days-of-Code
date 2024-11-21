number = int(input("Enter a number: "))
print("-----------------------------------")
print("MULTIPLICATION TABLE OF", number)

for i in range(1,13):
    table = i * number
    print(i, "X", number, "=", table)
    
print("-----------------------------------")