"""Chapter 05.1 — Modules and Imports

Key ideas:
- A module is a Python file that defines names.
- import module keeps names under the module namespace.
- from module import name imports a selected name.
- Use the main guard to separate reusable definitions from script execution.
"""

import math
from statistics import mean as calculate_mean

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

def main() -> None:
    print(f"Circle area: {circle_area(3):.2f}")
    print("Mean:", calculate_mean([10, 20, 30]))

if __name__ == "__main__":
    main()
