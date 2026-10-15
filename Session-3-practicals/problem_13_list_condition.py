# Problem 13: List and Condition
marks = [35, 48, 67, 82, 91]
target = int(input("Enter a mark: "))

if target in marks:
    print("That mark is in the list.")
    if target >= 35:
        print("It is a passing mark.")
    else:
        print("It is a failing mark.")
else:
    print("That mark is not in the list.")
