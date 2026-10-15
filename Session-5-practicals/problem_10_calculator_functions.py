def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

try:
    first = float(input("First number: "))
    second = float(input("Second number: "))
    operation = input("Choose +, -, *, or /: ").strip()
    if operation == "+": answer = add(first, second)
    elif operation == "-": answer = subtract(first, second)
    elif operation == "*": answer = multiply(first, second)
    elif operation == "/": answer = divide(first, second)
    else: raise ValueError("Unknown operation.")
    print("Result:", answer)
except (ValueError, ZeroDivisionError) as error:
    print("Calculator error:", error)
