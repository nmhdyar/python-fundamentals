"""
Chapter 01.2 — Input and Output

Key ideas:
- input() always returns a string.
- print() displays values.
- f-strings make formatted output readable.
- print() also supports sep and end.
"""

# Example 1: Ask for information and display a formatted message.
first_name = input("Enter your first name: ")
city = input("Which city do you live in? ")

print(f"Hello, {first_name}!")
print(f"Your city is {city}.")

print("\n" + "-" * 40 + "\n")

# Example 2: Format a small receipt.
product = input("Product name: ")
unit_price = input("Unit price: ")
quantity = input("Quantity: ")

# Conversion is intentionally covered in the next lesson.
unit_price = float(unit_price)
quantity = int(quantity)

total = unit_price * quantity

print("\nRECEIPT")
print("=" * 25)
print("Product:", product)
print("Unit price:", f"{unit_price:.2f}")
print("Quantity:", quantity)
print("Total:", f"{total:.2f}")

# sep controls the separator between values.
print("Python", "is", "fun", sep=" | ")

# end controls what print() adds at the end.
print("Loading", end="...")
print("Done!")
