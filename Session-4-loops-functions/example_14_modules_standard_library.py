# Standard library modules: math, random, datetime, os, pathlib

import math
import random
import os
from datetime import date, datetime
from pathlib import Path

print("Square root of 81:", math.sqrt(81))
print("Random dice roll:", random.randint(1, 6))
print("Today's date:", date.today())
print("Current date and time:", datetime.now())
print("Current working directory:", os.getcwd())
print("Current folder as a Path:", Path.cwd())
