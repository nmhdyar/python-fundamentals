"""Chapter 03.6 — Comprehensions

Key ideas:
- A list comprehension builds a list from an iterable.
- Add an if clause to filter items.
- A dictionary comprehension builds key-value pairs.
- Prefer a normal loop when a comprehension becomes difficult to read.
"""

# Example 1: Transform and filter numbers.
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
squares_of_evens: list[int] = [
    number ** 2 for number in numbers if number % 2 == 0
]
print("Even squares:", squares_of_evens)

# Example 2: Build a dictionary from names.
names: list[str] = ["sara", "ali", "nima"]
name_lengths: dict[str, int] = {
    name: len(name) for name in names
}
print("Name lengths:", name_lengths)
