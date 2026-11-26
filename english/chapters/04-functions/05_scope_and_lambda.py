"""Chapter 04.5 — Scope and Lambda

Key ideas:
- Local names are created inside a function.
- A function can read a global name, but changing global state is usually avoidable.
- lambda creates a small anonymous function expression.
- Sorting with key= is often clearer than writing a custom sorting loop.
"""

tax_rate: float = 0.09

def add_tax(amount: float) -> float:
    local_total = amount * (1 + tax_rate)
    return local_total

print(f"With tax: {add_tax(100):.2f}")

products: list[dict[str, object]] = [
    {"name": "Mouse", "price": 25.0},
    {"name": "Keyboard", "price": 49.0},
    {"name": "Webcam", "price": 39.0},
]
sorted_products = sorted(products, key=lambda item: item["price"])
print(sorted_products)
