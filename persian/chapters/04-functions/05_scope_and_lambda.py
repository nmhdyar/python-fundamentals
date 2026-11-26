"""فصل ۰۴.۵ — محدوده متغیرها و Lambda

نکته‌های کلیدی:
- نام‌های محلی داخل تابع ساخته می‌شوند.
- تابع می‌تواند نام سراسری را بخواند، اما معمولاً می‌توان از تغییر وضعیت سراسری پرهیز کرد.
- lambda یک عبارت تابعی کوچک و بدون نام ایجاد می‌کند.
- مرتب‌سازی با key= اغلب از نوشتن حلقه مرتب‌سازی اختصاصی روشن‌تر است.
"""

tax_rate: float = 0.09

def add_tax(amount: float) -> float:
    local_total = amount * (1 + tax_rate)
    return local_total

print(f"With tax: {add_tax(100):.2f}")

products: list[dict[str, object]] = [
    {"name": "Mouse", "price": 25.0},
    {"name": "Keyboard", "price": 49.0},
    {"name": "Webcam", "price": 39.0},
]
sorted_products = sorted(products, key=lambda item: item["price"])
print(sorted_products)
