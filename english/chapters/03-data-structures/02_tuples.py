"""Chapter 03.2 — Tuples

Key ideas:
- Tuples are ordered and immutable.
- A one-item tuple needs a trailing comma.
- Tuple unpacking assigns items to multiple names.
- Use tuples for fixed records or values that should not be reassigned by item.
"""

# Example 1: Store fixed coordinates.
point: tuple[float, float] = (10.5, 4.2)
x_coordinate, y_coordinate = point

print("X:", x_coordinate)
print("Y:", y_coordinate)

# Example 2: Return multiple values from a function.
def get_user() -> tuple[str, int]:
    return "Nima", 20

user_name, user_age = get_user()
print(f"{user_name} is {user_age} years old.")

# A one-item tuple:
single_value: tuple[str] = ("Python",)
print(single_value)
