# Problem 6: List Basics
fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

fruits.append("mango")
print("After adding mango:", fruits)

fruits[1] = "grapes"
print("After updating second item:", fruits)

fruits.remove("apple")
print("After removing apple:", fruits)
print("Number of fruits:", len(fruits))
