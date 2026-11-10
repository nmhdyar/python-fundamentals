"""
Chapter 02.6 — Counters and Accumulators

Key ideas:
- A counter tracks occurrences.
- An accumulator stores a result updated repeatedly.
- Initialize these variables before entering the loop.
"""

# Example 1: Calculate the sum from 1 through 100.
total = 0

for number in range(1, 101):
    total += number

print("Sum from 1 to 100:", total)

print("\n" + "-" * 40 + "\n")

# Example 2: Count numbers divisible by 3.
divisible_count = 0

for number in range(1, 31):
    if number % 3 == 0:
        divisible_count += 1

print("Numbers divisible by 3:", divisible_count)
