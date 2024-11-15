# ROOTS OF A QUADRATIC EQUATION
# ax^2 + bx + c
import math

a = float(input("Enter coefficient of x^2: "))
b = float(input("Enter coefficient of x: "))
c = float(input("Enter constant: "))

D = b**2 - 4 * a * c

if D < 0:
    print("There are no real roots")
elif D == 0:
    root_1 = (-b / 2 * a)
    root_2 = (-b / 2 * a)
    print("The roots are", round(root_1, 4), round(root_2, 4))
else:
    root_1 = (-b + math.sqrt(D)/ 2 * a)
    root_2 = (-b - math.sqrt(D)/ 2 * a)
    print("The roots are", round(root_1, 4), round(root_2, 4))



