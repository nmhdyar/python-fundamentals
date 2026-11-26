"""Chapter 03.4 — Dictionaries

Key ideas:
- A dictionary maps unique hashable keys to values.
- Use [] when a key must exist; use get() when it may be missing.
- keys(), values(), and items() expose dictionary views.
- update(), pop(), and the in operator are common operations.
"""

# Example 1: Read and update a product.
product: dict[str, object] = {
    "name": "Keyboard",
    "price": 49.90,
    "stock": 12,
}

print("Product:", product["name"])
print("Category:", product.get("category", "Uncategorized"))

product["stock"] = 10
product["category"] = "Accessories"
print("Updated product:", product)

# Example 2: Count word occurrences.
words: list[str] = ["python", "api", "python", "web", "api", "python"]
word_counts: dict[str, int] = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(f"{word}: {count}")
