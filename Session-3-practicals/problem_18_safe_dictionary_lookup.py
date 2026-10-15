# Problem 18: Safe Dictionary Lookup
student = {"name": "Anjali", "age": 21}

print("Name:", student["name"])
print("Email:", student.get("email", "Email not provided"))

removed_age = student.pop("age", None)
print("Removed age:", removed_age)
print("Remaining record:", student)
print("'name' exists:", "name" in student)
