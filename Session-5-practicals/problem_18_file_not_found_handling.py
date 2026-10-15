filename = input("Enter filename to read (default: missing.txt): ").strip() or "missing.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print(f"File not found: {filename}")
