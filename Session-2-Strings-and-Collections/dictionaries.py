# Session 2 Example 5: Dictionaries

student = {
    "name": "Asha",
    "age": 16,
    "marks": 88
}

print("Name:", student["name"])
print("Marks:", student["marks"])

student["marks"] = 93
student["city"] = "Vijayapura"

print("Updated student:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Email:", student.get("email", "Email not provided"))
