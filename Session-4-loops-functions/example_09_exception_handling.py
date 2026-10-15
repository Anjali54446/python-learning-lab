# try / except / else / finally

try:
    number = int(input("Enter a whole number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid whole number.")
except ZeroDivisionError:
    print("The number must not be zero.")
else:
    print("Result:", result)
finally:
    print("Input attempt finished.")
