# Session 2 Example 4: Sets

attendance_ids = [101, 102, 101, 103, 102, 104]
unique_ids = set(attendance_ids)
print("Original IDs:", attendance_ids)
print("Unique IDs:", sorted(unique_ids))

morning_group = {101, 102, 103}
afternoon_group = {103, 104, 105}

print("In both groups:", sorted(morning_group & afternoon_group))
print("In either group:", sorted(morning_group | afternoon_group))
print("Only in morning:", sorted(morning_group - afternoon_group))
