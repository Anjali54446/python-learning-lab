def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

try:
    n = int(input("Enter a non-negative integer: "))
    print(f"{n}! = {factorial(n)}")
except ValueError as error:
    print("Input error:", error)
