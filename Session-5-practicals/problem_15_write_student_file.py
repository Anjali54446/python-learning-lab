name = input("Student name: ")
age = input("Student age: ")
branch = input("Student branch: ")

with open("student_info.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\nAge: {age}\nBranch: {branch}\n")
print("Student information saved to student_info.txt")
