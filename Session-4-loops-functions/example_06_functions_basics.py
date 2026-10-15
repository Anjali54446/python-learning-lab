# Functions: define, call, parameters, and return

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(greet("Asha"))
print("Sum:", add(10, 5))
print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))
