"""
Chapter 02.2 — Iterating with a for Loop

Key ideas:
- A for loop visits items from an iterable.
- range(stop) starts at 0 and excludes stop.
- range(start, stop, step) controls the generated sequence.
"""

# Example 1: Iterate over a list.
languages = ["Python", "JavaScript", "Java", "C++"]

for language in languages:
    print("I am learning:", language)

print("\n" + "-" * 40 + "\n")

# Example 2: Generate a sequence of even numbers.
for number in range(2, 11, 2):
    print(number)

# The stop value (11) is not included.
