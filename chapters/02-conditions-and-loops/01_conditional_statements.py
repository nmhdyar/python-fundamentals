"""
Chapter 02.1 — Conditional Statements

Key ideas:
- if runs a block when its condition is True.
- elif checks another condition if earlier branches did not match.
- else handles every remaining case.
- Conditions are checked from top to bottom.
"""

# Example 1: Classify an age.
age = 20

if age < 0:
    print("Invalid age.")
elif age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

print("\n" + "-" * 40 + "\n")

# Example 2: Validate a score and assign a result.
score = 87

if not 0 <= score <= 100:
    print("Invalid score.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs improvement")

# Remember: == compares values; = assigns a value.
