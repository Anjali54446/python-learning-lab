# Loop demo: find a number in a list

numbers = [4, 8, 15, 16, 23, 42]
target = int(input("Enter a number to find: "))

found = False
for number in numbers:
    if number == target:
        found = True
        break

if found:
    print(f"{target} was found.")
else:
    print(f"{target} was not found.")
