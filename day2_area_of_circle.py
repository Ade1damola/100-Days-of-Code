# Import the value of pi
from math import pi

# Input the radius of the circle
r = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
a = pi * (r ** 2)

# Calculate the circumfrence of the circle 
c = 2 * pi * r

# Print the value for area and circumference
print("The area of the circle is " + str(round(a, 4)))
print("The circumference of the circle is " + str(round(c, 4)))
