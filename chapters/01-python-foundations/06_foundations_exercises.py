"""
Chapter 01.6 — Foundations Practice

Try each task yourself before reading the suggested solution.
"""

# Exercise 1: Personal profile
# Ask the user for their name, age, and city.
# Display a neat profile and calculate their age next year.

print("EXERCISE 1 — PERSONAL PROFILE")

name = input("Name: ").strip()
age = int(input("Age: "))
city = input("City: ").strip()

print("\n" + "=" * 30)
print(f"PROFILE: {name.title()}")
print("=" * 30)
print(f"City: {city.title()}")
print(f"Current age: {age}")
print(f"Age next year: {age + 1}")

print("\n" + "-" * 40 + "\n")

# Exercise 2: Shopping calculator
# Ask for an item name, its price, and quantity.
# Calculate the subtotal, a 10% discount, and the final total.

print("EXERCISE 2 — SHOPPING CALCULATOR")

item_name = input("Item name: ").strip()
item_price = float(input("Item price: "))
item_quantity = int(input("Quantity: "))

subtotal = item_price * item_quantity
discount_rate = 0.10
discount_amount = subtotal * discount_rate
final_total = subtotal - discount_amount

print("\n" + "=" * 30)
print("SHOPPING SUMMARY")
print("=" * 30)
print(f"Item: {item_name.title()}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount (10%): -{discount_amount:.2f}")
print(f"Final total: {final_total:.2f}")

# Challenge:
# Add input validation so negative prices and quantities are rejected.
