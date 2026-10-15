# Problem 8: Sum and Average of List Values
marks = [72, 85, 91, 68, 79]

total = sum(marks)
average = total / len(marks) if marks else 0

print("Marks:", marks)
print("Total:", total)
print(f"Average: {average:.2f}")
