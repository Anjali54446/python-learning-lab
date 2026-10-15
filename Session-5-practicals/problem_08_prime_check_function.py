def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

value = int(input("Enter an integer: "))
print(f"{value} is prime." if is_prime(value) else f"{value} is not prime.")
