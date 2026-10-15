n = int(input("Enter an integer: "))
is_prime = n > 1
for divisor in range(2, n):
    if n % divisor == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not prime")
