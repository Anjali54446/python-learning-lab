# Session 2 Example 2: Lists

shopping_list = ["rice", "milk", "apples"]
print("Original list:", shopping_list)
print("First item:", shopping_list[0])

shopping_list.append("bread")
print("After append:", shopping_list)

shopping_list[1] = "curd"
print("After update:", shopping_list)

shopping_list.remove("rice")
print("After remove:", shopping_list)
print("Number of items:", len(shopping_list))
