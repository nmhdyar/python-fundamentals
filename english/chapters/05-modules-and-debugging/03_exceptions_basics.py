"""Chapter 05.3 — Understanding Exceptions

Key ideas:
- A syntax error prevents code from being parsed.
- An exception occurs while code is running.
- Common exceptions include ValueError, TypeError, ZeroDivisionError, KeyError, and IndexError.
- Read the exception type and the last traceback lines first.
"""

raw_age: str = "twenty"
try:
    age: int = int(raw_age)
    print("Age:", age)
except ValueError:
    print("The age must contain digits.")

values: list[int] = [10, 20]
try:
    print(values[4])
except IndexError as error:
    print("Index problem:", error)
