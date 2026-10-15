def largest_number(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for character in text:
        if character in vowels:
            count += 1
    return count

print("Largest:", largest_number([4, 19, 2, 31, 7]))
print("Vowels:", count_vowels("Python training"))
