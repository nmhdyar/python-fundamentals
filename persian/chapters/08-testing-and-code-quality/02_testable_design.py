def average(values: list[float]) -> float:
    if not values:
        raise ValueError("حداقل یک مقدار لازم است")
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
    print("ورودی خالی مدیریت شد")
print(result)
