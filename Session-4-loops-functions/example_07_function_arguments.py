# Default arguments, keyword arguments, *args, and **kwargs

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ravi"))
print(greet(name="Asha", greeting="Welcome"))

def add_many(*numbers):
    return sum(numbers)

print("Sum:", add_many(2, 4, 6, 8))

def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Meena", branch="CSE", city="Vijayapura")
