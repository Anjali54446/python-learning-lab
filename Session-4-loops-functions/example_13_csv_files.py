# Write and read a CSV file using Python's csv module

import csv

rows = [
    ["name", "score"],
    ["Asha", 92],
    ["Ravi", 85],
]

with open("scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
