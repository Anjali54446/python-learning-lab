# Write (overwrite/create) and read a text file

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python basics\n")
    file.write("Functions make code reusable.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
