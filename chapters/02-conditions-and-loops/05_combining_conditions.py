"""
Chapter 02.5 — Combining Conditions

Use and when both conditions must be True.
"""

for number in range(1, 31):
    is_even = number % 2 == 0
    is_greater_than_ten = number > 10

    if is_even and is_greater_than_ten:
        print("Matching number:", number)
