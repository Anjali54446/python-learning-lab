# Guided practice examples from the slides

# 1. Print squares from 1 through 5.
for number in range(1, 6):
    print(number ** 2)

# 2. Convert Celsius to Fahrenheit using a function.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print("20°C =", celsius_to_fahrenheit(20), "°F")

# 3. Build a list of even numbers with a comprehension.
evens = [number for number in range(1, 21) if number % 2 == 0]
print("Even numbers:", evens)

# 4. Safely convert user input.
try:
    value = int(input("Enter a whole number: "))
except ValueError:
    print("That was not a whole number.")
else:
    print("You entered:", value)

# 5. Write three lines to a file and read them.
with open("practice.txt", "w", encoding="utf-8") as file:
    file.write("First line\nSecond line\nThird line\n")

with open("practice.txt", "r", encoding="utf-8") as file:
    print(file.read())

# 6. Display today's date.
from datetime import date
print("Today:", date.today())
