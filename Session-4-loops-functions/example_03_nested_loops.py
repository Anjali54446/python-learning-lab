# Nested loops: the inner loop runs for each outer-loop iteration

for row in range(1, 4):
    for column in range(1, 4):
        print(f"row={row}, column={column}")

print("\nMultiplication grid:")
for n in range(1, 4):
    for m in range(1, 4):
        print(n * m, end="\t")
    print()
