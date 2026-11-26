"""Chapter 04.6 — Recursion, Docstrings, and Annotations

Key ideas:
- A recursive function calls itself with a smaller or simpler problem.
- Every valid recursive design needs a base case.
- Docstrings describe a function's purpose and behavior.
- Type hints document expectations; Python does not enforce them automatically.
"""

def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("number must not be negative")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)

def countdown(number: int) -> None:
    """Print numbers down to zero."""
    if number < 0:
        return
    print(number)
    if number > 0:
        countdown(number - 1)

print("5! =", factorial(5))
countdown(3)
