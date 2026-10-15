import csv

rows = [["name", "score"], ["Asha", 92], ["Ravi", 85], ["Meena", 89]]
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.reader(file):
        print(row)
