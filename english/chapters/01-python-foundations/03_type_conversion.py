"""
Chapter 01.3 — Type Conversion

Key ideas:
- int(), float(), and str() convert compatible values.
- input() returns str, so numeric input usually needs conversion.
- bool() follows truth-value rules; non-empty strings are True.
- Invalid conversions can raise ValueError.
"""

# Example 1: Convert user input before doing arithmetic.
age_text: str = input("Enter your age: ")
age: int = int(age_text)

next_year_age: int = age + 1

print(f"Next year, you will be {next_year_age}.")

height_text: str = input("Enter your height in meters (e.g. 1.82): ")
height: float = float(height_text)

print(f"Your height is {height:.2f} meters.")

print("\n" + "-" * 40 + "\n")

# Example 2: Convert values and understand boolean conversion.
score: float = 87.9
whole_score: int = int(score)  # int() removes the decimal part; it does not round.
score_text: str = str(score)

print("Original:", score, type(score))
print("As integer:", whole_score, type(whole_score))
print("As text:", score_text, type(score_text))

print(bool(0))       # False
print(bool(12))      # True
print(bool(""))      # False
print(bool("False")) # True: this is a non-empty string!

# For real applications, validate user input before converting it.
