def average(values: list[float]) -> float:
    if not values:
        raise ValueError("at least one value is required")
    return sum(values) / len(values)


# Arrange
scores = [12.0, 18.0]
# Act
result = average(scores)
# Assert
assert result == 15.0

try:
    average([])
except ValueError:
    print("Empty input handled")
print(result)
