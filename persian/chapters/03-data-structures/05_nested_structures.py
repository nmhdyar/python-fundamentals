"""فصل ۰۳.۵ — ساختارهای داده تو در تو

نکته‌های کلیدی:
- یک مجموعه می‌تواند مجموعه دیگری را در خود نگه دارد.
- لیستی از دیکشنری‌ها برای نگهداری رکوردها کاربردی است.
- ساختار را مرحله‌به‌مرحله و از یک سطح به سطح بعد دنبال کن.
- پیش از اتکا به وجود یک کلید یا اندیس، آن را بررسی کن.
"""

# مثال ۱: کار با لیستی از رکوردهای محصول
products: list[dict[str, object]] = [
    {"name": "Mouse", "price": 25.0, "stock": 8},
    {"name": "Keyboard", "price": 49.0, "stock": 4},
]

for product in products:
    print(f"{product['name']}: {product['stock']} in stock")

# مثال ۲: خواندن امن داده تو در تو
school: dict[str, object] = {
    "name": "Central School",
    "students": [
        {"name": "Sara", "scores": [18, 19, 20]},
        {"name": "Ali", "scores": [15, 17, 16]},
    ],
}

students = school.get("students", [])
if students:
    first_student = students[0]
    print("First student:", first_student["name"])
    print("Scores:", first_student["scores"])
