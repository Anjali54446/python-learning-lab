# Session 2 Example 6: Nested Data

students = [
    {"name": "Asha", "marks": 93},
    {"name": "Ravi", "marks": 81},
    {"name": "Meena", "marks": 88}
]

print("Second student's name:", students[1]["name"])
print("First student's marks:", students[0]["marks"])

students.append({"name": "Arun", "marks": 90})
print("Number of students:", len(students))
print("New student:", students[3])
