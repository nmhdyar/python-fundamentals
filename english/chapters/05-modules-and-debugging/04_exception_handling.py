"""Chapter 05.4 — Handling Exceptions

Key ideas:
- Put only the risky operation inside the try block.
- Catch specific exceptions rather than using a bare except.
- else runs when no exception occurs.
- finally runs whether an exception occurred or not.
"""

def parse_quantity(text: str) -> int | None:
    try:
        quantity = int(text)
    except ValueError:
        print("Quantity must be a whole number.")
        return None
    else:
        if quantity < 0:
            print("Quantity cannot be negative.")
            return None
        return quantity
    finally:
        print("Input check finished.")

print("Result:", parse_quantity("4"))
print("Result:", parse_quantity("four"))
