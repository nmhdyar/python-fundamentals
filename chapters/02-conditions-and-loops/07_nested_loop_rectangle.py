"""
Chapter 02.7 — Nested Loops

Key ideas:
- A nested loop is a loop inside another loop.
- The outer loop commonly controls rows.
- The inner loop commonly controls columns.
- The inner loop finishes before the outer loop advances.
"""

# Example 1: Draw a rectangle.
rows: int = 3
columns: int = 5

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()

print("\n" + "-" * 40 + "\n")

# Example 2: Print row and column coordinates.
first_index: int = 1
last_index: int = 4

for row in range(first_index, last_index):
    for column in range(first_index, last_index):
        print(f"({row}, {column})", end=" ")
    print()
