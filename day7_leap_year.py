# Step-by-Step Logic
# Check if the year is divisible by 400.
#   If it is, then it is a leap year.
# If the year is not divisible by 400, check if it is divisible by 100.
#   If it is, then it is not a leap year.
# If the year is not divisible by 100, check if it is divisible by 4.
#   If it is, then it is a leap year.
#   If it is not, then it is not a leap year.

year = int(input("Enter the year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(year, " is a leap year")
    else: 
        print(year, " is not a leap year")
elif year % 4 == 0:
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")