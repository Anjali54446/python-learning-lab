# Integrated demo: read a document, handle missing file, count characters and words

def count_words(text):
    return len(text.split())

# Create a sample document so this demo runs immediately.
with open("sample_document.txt", "w", encoding="utf-8") as file:
    file.write("Python file handling is useful.\n")
    file.write("It is an early step in preparing documents for RAG.\n")

try:
    with open("sample_document.txt", "r", encoding="utf-8") as file:
        document = file.read()
except FileNotFoundError:
    print("Create sample_document.txt first.")
else:
    print("Characters:", len(document))
    print("Words:", count_words(document))
