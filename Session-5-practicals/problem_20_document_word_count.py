def count_words(text):
    return len(text.split())

with open("sample_document.txt", "w", encoding="utf-8") as file:
    file.write("Python makes it possible to read and process documents.\n")
    file.write("Document processing is one step in a RAG workflow.\n")

try:
    with open("sample_document.txt", "r", encoding="utf-8") as file:
        document = file.read()
except FileNotFoundError:
    print("Create sample_document.txt first.")
else:
    print("Characters:", len(document))
    print("Words:", count_words(document))
