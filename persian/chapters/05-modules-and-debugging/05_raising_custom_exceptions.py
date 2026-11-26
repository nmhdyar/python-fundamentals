"""فصل ۰۵.۵ — ایجاد استثنا و استثنای اختصاصی

نکته‌های کلیدی:
- raise اعلام می‌کند تابع با ورودی فعلی نمی‌تواند درخواست را کامل کند.
- وقتی یک استثنای داخلی مشکل را دقیق توصیف می‌کند، همان را انتخاب کن.
- استثنای اختصاصی می‌تواند یک خطای مربوط به دامنه برنامه را نمایش دهد.
- از استثنا به‌جای بررسی شرط‌های عادی استفاده نکن.
"""

class InsufficientStockError(Exception):
    """وقتی سفارش از موجودی قابل دسترس بیشتر باشد ایجاد می‌شود."""

def reserve_stock(available: int, requested: int) -> int:
    if requested < 0:
        raise ValueError("requested quantity cannot be negative")
    if requested > available:
        raise InsufficientStockError("not enough stock")
    return available - requested

print("Remaining:", reserve_stock(10, 3))

try:
    reserve_stock(2, 5)
except InsufficientStockError as error:
    print("Reservation failed:", error)
