# List and dictionary comprehensions

squares = [number ** 2 for number in range(1, 6)]
print("Squares:", squares)

even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print("Even numbers:", even_numbers)

square_lookup = {number: number ** 2 for number in range(1, 6)}
print("Number-to-square dictionary:", square_lookup)
