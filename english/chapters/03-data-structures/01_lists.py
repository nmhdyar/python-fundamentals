"""Chapter 03.1 — Lists

Key ideas:
- Lists are ordered and mutable.
- Indexing starts at zero; negative indexes count from the end.
- Slicing creates a new list.
- append(), extend(), insert(), remove(), pop(), sort(), and copy() are common tools.
"""

# Example 1: Read and update a shopping list.
shopping_list: list[str] = ["bread", "milk", "eggs"]
print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])

shopping_list.append("coffee")
shopping_list[1] = "oat milk"
print("Updated list:", shopping_list)

# Example 2: Slice and sort without changing the original list.
scores: list[int] = [72, 95, 81, 68, 88]
top_scores: list[int] = sorted(scores, reverse=True)[:3]

print("Original scores:", scores)
print("Top three:", top_scores)
