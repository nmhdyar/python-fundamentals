"""
Chapter 02.8 — Conditional Output with Nested Loops

Key ideas:
- Each nested-loop iteration has a row and column index.
- Indexes start at 0 when using range(number).
- Combining indexes with modulo can create repeating patterns.
- Annotate dimensions as int; loop indexes are inferred as int.
"""

rows: int = 6
columns: int = 8

for row in range(rows):
    for column in range(columns):
        if (row + column) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Try changing rows and columns.
# Explain why neighboring cells alternate.
