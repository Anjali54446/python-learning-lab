# Problem 2: Simple Calculator
a = float(input("First number: "))
b = float(input("Second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division is not possible because the second number is zero.")
