text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0
for character in text:
    if character in vowels:
        count += 1
print("Vowel count:", count)
