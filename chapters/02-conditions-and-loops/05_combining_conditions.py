"""
Chapter 02.5 — Combining Conditions

Key ideas:
- and: every condition must be True.
- or: at least one condition must be True.
- not: reverses a boolean value.
- Parentheses can make complex expressions easier to read.
"""

# Example 1: Find even numbers greater than 10.
for number in range(1, 31):
    is_even: bool = number % 2 == 0
    is_greater_than_ten: bool = number > 10

    if is_even and is_greater_than_ten:
        print("Matching number:", number)

print("\n" + "-" * 40 + "\n")

# Example 2: Decide whether a visitor can enter.
age: int = 20
has_ticket: bool = False
is_vip: bool = True

if age >= 18 and (has_ticket or is_vip):
    print("Entry allowed.")
else:
    print("Entry denied.")
