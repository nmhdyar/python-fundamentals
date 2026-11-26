"""Chapter 03.5 — Nested Data Structures

Key ideas:
- Collections can contain other collections.
- A list of dictionaries is useful for records.
- Follow the structure one level at a time.
- Check that a key or index exists before relying on it.
"""

# Example 1: Work with a list of product records.
products: list[dict[str, object]] = [
    {"name": "Mouse", "price": 25.0, "stock": 8},
    {"name": "Keyboard", "price": 49.0, "stock": 4},
]

for product in products:
    print(f"{product['name']}: {product['stock']} in stock")

# Example 2: Read nested data safely.
school: dict[str, object] = {
    "name": "Central School",
    "students": [
        {"name": "Sara", "scores": [18, 19, 20]},
        {"name": "Ali", "scores": [15, 17, 16]},
    ],
}

students = school.get("students", [])
if students:
    first_student = students[0]
    print("First student:", first_student["name"])
    print("Scores:", first_student["scores"])
