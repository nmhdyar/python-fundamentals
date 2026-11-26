"""فصل ۰۴.۲ — پارامترها و مقادیر بازگشتی

نکته‌های کلیدی:
- پارامتر نامی در تعریف تابع است؛ آرگومان مقداری است که هنگام فراخوانی فرستاده می‌شود.
- return نتیجه را به فراخواننده برمی‌گرداند.
- print() مقدار را نمایش می‌دهد، اما جای return را نمی‌گیرد.
- return زودهنگام می‌تواند ورودی نامعتبر را روشن و ساده مدیریت کند.
"""

def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

def calculate_average(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)

subtotal: float = calculate_total(12.5, 4)
tax: float = subtotal * 0.09
print(f"Final total: {subtotal + tax:.2f}")

average = calculate_average([18.0, 16.5, 20.0])
if average is None:
    print("No scores available.")
else:
    print(f"Average: {average:.2f}")
