"""Chapter 04.4 — *args and **kwargs

Key ideas:
- *args collects extra positional arguments into a tuple.
- **kwargs collects extra keyword arguments into a dictionary.
- The * and ** operators can also unpack collections in a call.
- Use these features when a function genuinely needs a flexible interface.
"""

def calculate_sum(*numbers: int) -> int:
    return sum(numbers)

def show_settings(**settings: object) -> None:
    for key, value in settings.items():
        print(f"{key}: {value}")

print("Sum:", calculate_sum(2, 4, 6, 8))
show_settings(theme="dark", notifications=True, font_size=14)

options: dict[str, object] = {"theme": "light", "notifications": False}
show_settings(**options)
