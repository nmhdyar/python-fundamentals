"""
Chapter 02.4 — Filtering with Conditions

Key ideas:
- The modulo operator (%) returns a remainder.
- number % 2 == 0 means the number is even.
- number % 2 != 0 means the number is odd.
- A condition inside a loop filters which items are processed.
"""

# Example 1: Print even numbers from 1 through 20.
start: int = 1\nstop: int = 21\n\nfor number in range(start, stop):
    if number % 2 == 0:
        print("Even:", number)

print("\n" + "-" * 40 + "\n")

# Example 2: Print odd numbers from 1 through 15.
for number in range(1, 16):
    if number % 2 != 0:
        print("Odd:", number)
