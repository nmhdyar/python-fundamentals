"""Chapter 04.1 — Defining Functions

Key ideas:
- def creates a function object.
- The function body runs only when the function is called.
- Keep one function focused on one responsibility.
- pass is a placeholder, not a completed implementation.
"""

def greet_user() -> None:
    """Print a short greeting."""
    print("Welcome to Python!")

def show_separator() -> None:
    print("-" * 30)

greet_user()
show_separator()
greet_user()

def show_menu() -> None:
    print("1. View products")
    print("2. Add product")
    print("3. Exit")

show_menu()
