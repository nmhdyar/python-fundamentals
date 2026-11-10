"""
Chapter 02.6 — Accumulating a Sum

An accumulator stores a running result as a loop progresses.
"""

total = 0

for number in range(1, 101):
    total += number

print("Sum from 1 to 100:", total)
