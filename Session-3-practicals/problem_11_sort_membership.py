# Problem 11: Sort and Membership
marks = [72, 45, 91, 68, 55]
marks.sort()
print("Sorted marks:", marks)

target = int(input("Enter a mark to search for: "))
if target in marks:
    print(f"{target} is present.")
else:
    print(f"{target} is not present.")
