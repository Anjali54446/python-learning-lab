# Session 2 Example 1: Strings

message = "Hello Python"
print("Original:", message)

# Indexing
print("First character:", message[0])
print("Last character:", message[-1])

# Slicing
print("First five characters:", message[:5])
print("From index 6:", message[6:])

# Common methods
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Replace:", message.replace("Python", "World"))
print("Words:", message.split())

name = "Asha"
print(f"Welcome, {name}!")
