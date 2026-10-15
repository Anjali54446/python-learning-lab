import math

def circle_area(radius):
    return math.pi * radius ** 2

radius = float(input("Enter circle radius: "))
if radius < 0:
    print("Radius cannot be negative.")
else:
    print(f"Area: {circle_area(radius):.2f}")
