"""Chapter 04.2 — Parameters and Return Values

Key ideas:
- Parameters are names in a function definition; arguments are supplied values.
- return sends a result back to the caller.
- print() displays a value but does not replace return.
- An early return can handle invalid input clearly.
"""

def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

def calculate_average(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)

subtotal: float = calculate_total(12.5, 4)
tax: float = subtotal * 0.09
print(f"Final total: {subtotal + tax:.2f}")

average = calculate_average([18.0, 16.5, 20.0])
if average is None:
    print("No scores available.")
else:
    print(f"Average: {average:.2f}")
