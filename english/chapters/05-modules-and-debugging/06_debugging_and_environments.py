"""Chapter 05.6 — Debugging and Virtual Environments

Key ideas:
- Reproduce the problem with the smallest reliable input.
- Read the traceback from the bottom upward to find the exception and failing line.
- Inspect variable values and verify assumptions.
- Use a virtual environment to isolate project dependencies.

Typical terminal commands (run in your project folder):
    python -m venv .venv
    # Windows PowerShell:
    .venv\\Scripts\\Activate.ps1
    # macOS/Linux:
    source .venv/bin/activate
    python -m pip install requests
    python -m pip freeze
"""

def calculate_unit_price(total: float, quantity: int) -> float:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return total / quantity

try:
    print("Unit price:", calculate_unit_price(120, 4))
except ValueError as error:
    print("Invalid calculation:", error)

cart: dict[str, int] = {"mouse": 2, "keyboard": 1}
print("DEBUG cart contents:", cart)
print("Total items:", sum(cart.values()))
