class Product:
    def __init__(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("price cannot be negative")
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: ${self.price:.2f}"

product = Product("Keyboard", 49.9)
print(product)
