class Product:
    def __init__(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("قیمت نمی‌تواند منفی باشد")
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: ${self.price:.2f}"

product = Product("صفحه‌کلید", 49.9)
print(product)
