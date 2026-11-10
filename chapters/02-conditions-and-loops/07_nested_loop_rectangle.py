"""
Chapter 02.7 — Nested Loops

Key ideas:
- A nested loop is a loop inside another loop.
- The outer loop commonly controls rows.
- The inner loop commonly controls columns.
- The inner loop finishes before the outer loop advances.
"""

# Example 1: Draw a rectangle.
rows = 3
columns = 5

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()

print("\n" + "-" * 40 + "\n")

# Example 2: Print row and column coordinates.
for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")
    print()
