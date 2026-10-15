# Problem 4: String Operations
sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Character count:", len(sentence))
print("First character:", sentence[0] if sentence else "(empty string)")
print("Last character:", sentence[-1] if sentence else "(empty string)")
print("Words:", sentence.split())
