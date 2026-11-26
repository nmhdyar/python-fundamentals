"""فصل ۰۴.۴ — آرگومان‌های *args و **kwargs

نکته‌های کلیدی:
- *args آرگومان‌های موقعیتی اضافه را در یک تاپل جمع می‌کند.
- **kwargs آرگومان‌های نام‌دار اضافه را در یک دیکشنری جمع می‌کند.
- عملگرهای * و ** برای بازکردن مجموعه‌ها هنگام فراخوانی نیز کاربرد دارند.
- فقط وقتی از این قابلیت‌ها استفاده کن که تابع واقعاً به رابط انعطاف‌پذیر نیاز دارد.
"""

def calculate_sum(*numbers: int) -> int:
    return sum(numbers)

def show_settings(**settings: object) -> None:
    for key, value in settings.items():
        print(f"{key}: {value}")

print("Sum:", calculate_sum(2, 4, 6, 8))
show_settings(theme="dark", notifications=True, font_size=14)

options: dict[str, object] = {"theme": "light", "notifications": False}
show_settings(**options)
