while True:
    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("That is not a valid whole number. Try again.")
    else:
        print("You entered:", number)
        break
