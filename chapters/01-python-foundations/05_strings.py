"""
Chapter 01.5 — Strings

Key ideas:
- Strings are sequences of characters.
- Indexing starts at 0; negative indexes count from the end.
- Slicing uses [start:stop:step]; stop is excluded.
- Strings are immutable: methods return new strings.
- f-strings are a clear way to format values.
"""

# Example 1: Indexing, slicing, and string length.
language = "Python"

print("First character:", language[0])
print("Last character:", language[-1])
print("First three:", language[0:3])
print("From index 2:", language[2:])
print("Reversed:", language[::-1])
print("Length:", len(language))

print("\n" + "-" * 40 + "\n")

# Example 2: Clean and format user-provided text.
raw_name = "   nImA mahdiYar   "

clean_name = raw_name.strip()
display_name = clean_name.title()
username = clean_name.lower().replace(" ", "_")

print("Original:", repr(raw_name))
print("Clean name:", display_name)
print("Username:", username)
print("Starts with Nima:", display_name.startswith("Nima"))
print("Contains a space:", " " in display_name)

# Strings are immutable. This creates a new string; it does not edit the old one.
message = "hello"
message = message.upper()
print(f"Updated message: {message}")
