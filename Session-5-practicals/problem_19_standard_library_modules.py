import math
import random
from datetime import date, datetime

number = float(input("Enter a non-negative number for square root: "))
if number < 0:
    print("Square root example requires a non-negative number.")
else:
    print("Square root:", math.sqrt(number))
print("Random dice roll:", random.randint(1, 6))
print("Today's date:", date.today())
print("Current date and time:", datetime.now())
