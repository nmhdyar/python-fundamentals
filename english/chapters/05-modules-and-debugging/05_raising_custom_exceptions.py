"""Chapter 05.5 — Raising and Custom Exceptions

Key ideas:
- raise signals that a function cannot complete a request as given.
- Choose a meaningful built-in exception when it describes the problem.
- A custom exception can represent a domain-specific failure.
- Do not use exceptions instead of ordinary condition checks.
"""

class InsufficientStockError(Exception):
    """Raised when an order asks for more stock than available."""

def reserve_stock(available: int, requested: int) -> int:
    if requested < 0:
        raise ValueError("requested quantity cannot be negative")
    if requested > available:
        raise InsufficientStockError("not enough stock")
    return available - requested

print("Remaining:", reserve_stock(10, 3))

try:
    reserve_stock(2, 5)
except InsufficientStockError as error:
    print("Reservation failed:", error)
