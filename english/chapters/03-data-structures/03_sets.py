"""Chapter 03.3 — Sets

Key ideas:
- Sets store unique hashable values and do not provide positional indexing.
- Use set() for an empty set; {} creates an empty dictionary.
- Membership checks are useful for fast lookups.
- Union, intersection, and difference compare collections.
"""

# Example 1: Remove duplicate tags.
tags: list[str] = ["python", "web", "python", "api", "web"]
unique_tags: set[str] = set(tags)

print("Unique tags:", unique_tags)
print("Has API tag:", "api" in unique_tags)

# Example 2: Compare course registrations.
morning_group: set[str] = {"Sara", "Ali", "Nima"}
evening_group: set[str] = {"Nima", "Mina", "Reza"}

print("All students:", morning_group | evening_group)
print("Both groups:", morning_group & evening_group)
print("Morning only:", morning_group - evening_group)
