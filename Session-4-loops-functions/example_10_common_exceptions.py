# Common exceptions: ValueError, TypeError, ZeroDivisionError

examples = [
    ("ValueError", lambda: int("hello")),
    ("TypeError", lambda: "age" + 10),
    ("ZeroDivisionError", lambda: 10 / 0),
]

for label, operation in examples:
    try:
        operation()
    except (ValueError, TypeError, ZeroDivisionError) as error:
        print(f"{label}: {error}")
