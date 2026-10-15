age = 20
has_id = True

print("Adult:", age >= 18)
print("Can enter:", age >= 18 and has_id)
print("Needs guardian:", age < 18 or not has_id)
