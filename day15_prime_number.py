number = int(input("Enter the number: "))

factor = 0
for i in range(1, number + 1):
    if number % i == 0:
        factor += 1
if factor == 2:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")