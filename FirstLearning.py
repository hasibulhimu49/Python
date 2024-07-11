unit = float(input("Enter the unit: "))
bill = 0.0

if unit <= 50:
    bill = unit * 0.50
elif unit <= 150:
    bill = (50 * 0.50) + ((unit - 50) * 0.75)
elif unit <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((unit - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 2.20) + ((unit-250) * 1.50)

surcharge = bill * 0.20
Total_bill = bill + surcharge

print(f"Total bill is: {Total_bill}")