# Problem 16: Compare Two Skill Sets
team_a = {"Python", "SQL", "AI"}
team_b = {"SQL", "AI", "Cloud"}

print("Common skills:", sorted(team_a & team_b))
print("All skills:", sorted(team_a | team_b))
print("Only in Team A:", sorted(team_a - team_b))
