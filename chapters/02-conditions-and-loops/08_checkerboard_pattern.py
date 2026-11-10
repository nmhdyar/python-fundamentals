"""
Chapter 02.8 — Checkerboard Pattern with Nested Loops

The sum of the row and column indexes determines which positions
contain a star. No delay is needed to display the pattern.
"""

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for row in range(rows):
    for column in range(columns):
        if (row + column) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
