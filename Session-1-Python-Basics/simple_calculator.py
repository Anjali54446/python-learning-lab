number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

print(f"Sum: {number_1 + number_2}")
print(f"Difference: {number_1 - number_2}")
print(f"Product: {number_1 * number_2}")

if number_2 != 0:
    print(f"Quotient: {number_1 / number_2}")
else:
    print("Cannot divide by zero.")
