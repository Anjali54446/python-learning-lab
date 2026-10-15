# break, continue, and pass

print("break stops the loop:")
for number in range(1, 6):
    if number == 4:
        break
    print(number)

print("\ncontinue skips the current iteration:")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

print("\npass is a placeholder:")
for number in range(1, 4):
    if number == 2:
        pass  # No action yet; execution continues.
    print(number)
