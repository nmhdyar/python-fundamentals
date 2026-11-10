"""
Chapter 02.3 — while Loops

Key ideas:
- A while loop repeats while its condition remains True.
- Update the state used by the condition.
- Make sure the loop has a reachable stopping condition.
"""

# Example 1: Count from 1 to 5.
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print("\n" + "-" * 40 + "\n")

# Example 2: Repeat until the target is reached.
target = 4
guess = 0

while guess != target:
    guess += 1
    print("Current guess:", guess)

print("Target reached!")

# If guess were never updated, this loop could run forever.
