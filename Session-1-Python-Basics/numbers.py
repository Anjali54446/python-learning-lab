x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x > y:
    print(f"{x} is larger.")
elif y > x:
    print(f"{y} is larger.")
else:
    print("Both numbers are equal.")
