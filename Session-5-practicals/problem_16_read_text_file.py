with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python supports text file handling.\n")
    file.write("The with statement closes the file automatically.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
