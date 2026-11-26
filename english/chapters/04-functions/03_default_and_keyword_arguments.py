"""Chapter 04.3 — Default and Keyword Arguments

Key ideas:
- Default values make selected arguments optional.
- Keyword arguments make calls easier to read.
- Required parameters must come before parameters with defaults.
- Avoid mutable default values such as [] or {}.
"""

def create_profile(name: str, city: str = "Unknown", active: bool = True) -> dict[str, object]:
    return {"name": name, "city": city, "active": active}

profile_one = create_profile("Sara")
print(profile_one)

profile_two = create_profile("Nima", active=False, city="Shiraz")
print(profile_two)
