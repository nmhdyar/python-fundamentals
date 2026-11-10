"""
Chapter 01.1 — Variables and Data Types

Key ideas:
- A variable is a name that refers to a value.
- Python is dynamically typed: a variable can refer to values of different types.
- Use descriptive snake_case names.
- Common built-in types: int, float, str, bool, and NoneType.
"""

# Example 1: Create variables and inspect their types.
student_name = "Nima"
student_age = 20
student_height = 182.5
is_learning_python = True
middle_name = None

print("Student:", student_name)
print("Age:", student_age)
print("Height:", student_height)
print("Learning Python:", is_learning_python)

print(type(student_name))       # <class 'str'>
print(type(student_age))        # <class 'int'>
print(type(student_height))     # <class 'float'>
print(type(is_learning_python)) # <class 'bool'>
print(type(middle_name))        # <class 'NoneType'>

print("\n" + "-" * 40 + "\n")

# Example 2: Variables can be updated and reassigned.
product_name = "Keyboard"
price = 45.90
quantity = 3
in_stock = True

total_price = price * quantity

print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Total: {total_price:.2f}")

# Reassigning a variable changes the value it refers to.
quantity = 5
total_price = price * quantity

print(f"Updated quantity: {quantity}")
print(f"Updated total: {total_price:.2f}")

# Naming rules:
# - Start with a letter or underscore.
# - Do not use spaces or Python keywords.
# - Prefer descriptive snake_case names.
