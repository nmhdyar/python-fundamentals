"""فصل ۰۴.۱ — تعریف تابع

نکته‌های کلیدی:
- دستور def یک شیء تابع ایجاد می‌کند.
- بدنه تابع فقط هنگام فراخوانی اجرا می‌شود.
- هر تابع را روی یک مسئولیت مشخص متمرکز نگه دار.
- pass فقط جای‌نگهدار است و پیاده‌سازی کامل محسوب نمی‌شود.
"""

def greet_user() -> None:
    """نمایش یک پیام خوشامدگویی کوتاه."""
    print("Welcome to Python!")

def show_separator() -> None:
    print("-" * 30)

greet_user()
show_separator()
greet_user()

def show_menu() -> None:
    print("1. View products")
    print("2. Add product")
    print("3. Exit")

show_menu()
