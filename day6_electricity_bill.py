# Input: units_consumed, cost_per_unit, fixed_charge, tax_rate
units_consumed = float(input("Enter the amount of units consumed: "))
cost_per_unit = float(input("Enter the cost per unit: "))
fixed_charge = float(input("Enter the fixed charge: "))
tax_rate = float(input("Enter the tax rate: "))

# Calculate basic_charge = units_consumed * cost_per_unit
basic_charge = units_consumed * cost_per_unit

# Calculate total_charge_before_tax = basic_charge + fixed_charge
total_charge_before_tax = basic_charge + fixed_charge

# Calculate tax_amount = total_charge_before_tax * (tax_rate / 100)
tax_amount = total_charge_before_tax * (tax_rate / 100)

# Calculate total_bill = total_charge_before_tax + tax_amount
total_bill = total_charge_before_tax + tax_amount
 
print("---------------------------------------------------")
print("Amount of units consumed: ", units_consumed, "units")
print("Cost per unit: ", cost_per_unit)
print("Fixed charge: ", fixed_charge, "$/KW")
print("Tax rate: ", tax_rate)
print("Electricity bill is $",round(total_bill, 2))
print("---------------------------------------------------")