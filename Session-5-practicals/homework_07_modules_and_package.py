import math
import random
from datetime import datetime

print("Square root of 49:", math.sqrt(49))
print("Random number 1–100:", random.randint(1, 100))
print("Current date/time:", datetime.now())

# To create your own module, save this in my_helpers.py:
# def double(number):
#     return number * 2
#
# Then import it from another file/cell in the same folder:
# from my_helpers import double
# print(double(10))
#
# In a Google Colab code cell, install a third-party package:
# !pip install requests
# Then in a normal Python cell:
# import requests
# print(requests.__version__)
