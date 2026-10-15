# Independent Practice: solutions
# 1. First and last words in a sentence
sentence = input("Enter a sentence: ").strip()
words = sentence.split()
if words:
    print("First word:", words[0])
    print("Last word:", words[-1])
else:
    print("No words entered.")

# 2. Total and highest price
prices = [19.99, 5.50, 12.00, 8.75]
print("Price total:", sum(prices))
print("Highest price:", max(prices))

# 3. Common employee skills
employee_a = {"Python", "Excel", "SQL"}
employee_b = {"SQL", "Power BI", "Python"}
print("Common skills:", sorted(employee_a & employee_b))

# 4. Product dictionary and price update
product = {"name": "Notebook", "price": 45.0}
product["price"] = 50.0
print("Updated product:", product)

# 5. Nested student dictionary
student = {"name": "Meena", "marks": {"Python": 91, "SQL": 86}}
print("SQL mark:", student["marks"]["SQL"])
