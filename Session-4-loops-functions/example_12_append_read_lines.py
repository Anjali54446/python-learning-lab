# Append to a text file and read it line by line

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Files are useful for document processing.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
