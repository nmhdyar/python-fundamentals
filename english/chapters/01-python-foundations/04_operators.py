"""
Chapter 01.4 — Operators

Key ideas:
- Arithmetic: +, -, *, /, //, %, **
- Comparison: ==, !=, >, <, >=, <=
- Logical: and, or, not
- Assignment: =, +=, -=, *=, ...
- Parentheses make evaluation order explicit.
"""

# Example 1: Arithmetic operators.
first_number: int = 17
second_number: int = 5

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Floor division:", first_number // second_number)
print("Remainder:", first_number % second_number)
print("Power:", first_number ** 2)

print("\n" + "-" * 40 + "\n")

# Example 2: Combine comparison and logical operators in a decision.
age: int = 20
has_ticket: bool = True
is_vip: bool = False

is_adult: bool = age >= 18
can_enter: bool = is_adult and (has_ticket or is_vip)

print("Is adult:", is_adult)
print("Has ticket:", has_ticket)
print("VIP:", is_vip)
print("Can enter:", can_enter)

# Assignment operators update an existing variable.
balance: int = 100
balance += 25
balance -= 10
balance *= 2

print("Final balance:", balance)

# Prefer parentheses when an expression could be hard to read.
result: int = (10 + 5) * 2
print("Result:", result)
