# Integrated Challenge: Student Result
name = input("Student name: ")
marks = [
    float(input("Python marks: ")),
    float(input("SQL marks: ")),
    float(input("AI marks: "))
]

total = sum(marks)
average = total / len(marks)
result = "Pass" if all(mark >= 35 for mark in marks) else "Fail"

print("\n--- Student Result ---")
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")
print(f"Result: {result}")
