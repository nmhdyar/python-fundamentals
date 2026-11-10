"""
Chapter 02.4 — Filtering Even Numbers

The modulo operator (%) gives the remainder after division.
An integer is even when number % 2 equals 0.
"""

for number in range(1, 21):
    if number % 2 == 0:
        print("Even number:", number)
