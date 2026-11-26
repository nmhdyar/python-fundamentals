"""Chapter 05.2 — Useful Standard-Library Modules

Key ideas:
- The standard library ships with Python; it does not need a separate pip install.
- math provides mathematical functions and constants.
- random provides pseudo-random values; use secrets for security-sensitive tokens.
- datetime represents dates and times; pathlib works with filesystem paths.
"""

from datetime import date
from pathlib import Path
import math
import random

radius: float = 2.5
print(f"Area: {math.pi * radius ** 2:.2f}")
random.seed(7)
print("Sample:", random.randint(1, 6))

project_path: Path = Path("my_project")
print("Folder name:", project_path.name)
print("Today:", date.today())
