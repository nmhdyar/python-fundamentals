from typing import TypeAlias

Number: TypeAlias = int | float

def calculate_average(values: list[Number]) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)

print(calculate_average([12, 15.5, 18]))
