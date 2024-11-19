a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("It is an equilateral triangle")
elif a == b or b == c or c == a:
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")