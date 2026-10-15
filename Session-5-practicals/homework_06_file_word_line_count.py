filename = "journal.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("Python files preserve information.\n")
    file.write("We can read and append text.\n")

with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))

with open(filename, "a", encoding="utf-8") as file:
    file.write("This line was appended later.\n")
print("New information appended.")
