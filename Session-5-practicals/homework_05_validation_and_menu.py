def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
    choice = input("Choose an option: ").strip()
    if choice == "5":
        print("Goodbye!")
        break
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid menu option. Try again.")
        continue
    a = read_number("First number: ")
    b = read_number("Second number: ")
    if choice == "1": print("Result:", a + b)
    elif choice == "2": print("Result:", a - b)
    elif choice == "3": print("Result:", a * b)
    elif b == 0: print("Cannot divide by zero.")
    else: print("Result:", a / b)
