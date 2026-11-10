"""
Chapter 02.7 — Drawing a Rectangle with Nested Loops

The outer loop controls rows.
The inner loop controls columns.
"""

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()
