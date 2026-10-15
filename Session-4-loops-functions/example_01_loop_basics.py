# Loop basics: repeated code, for, range, and iterating over a string

print("Without a loop:")
print("Hello")
print("Hello")
print("Hello")

print("\nWith a loop:")
for count in range(3):
    print("Hello")

print("\nNumbers 1 to 5:")
for number in range(1, 6):
    print(number)

print("\nEven numbers from 2 to 10:")
for number in range(2, 11, 2):
    print(number)

print("\nLetters in AI:")
for letter in "AI":
    print(letter)
