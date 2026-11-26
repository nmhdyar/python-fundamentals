"""فصل ۰۵.۶ — اشکال‌زدایی و محیط مجازی

نکته‌های کلیدی:
- مشکل را با کوچک‌ترین ورودی قابل اعتماد بازتولید کن.
- Traceback را از پایین به بالا بخوان تا نوع استثنا و خط مشکل‌دار را پیدا کنی.
- مقدار متغیرها را بررسی و فرضیه‌ها را آزمایش کن.
- برای جدا نگه‌داشتن وابستگی‌های پروژه از محیط مجازی استفاده کن.

دستورهای معمول ترمینال (در پوشه پروژه اجرا کن):
    python -m venv .venv
    # Windows PowerShell:
    .venv\\Scripts\\Activate.ps1
    # macOS/Linux:
    source .venv/bin/activate
    python -m pip install requests
    python -m pip freeze
"""

def calculate_unit_price(total: float, quantity: int) -> float:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return total / quantity

try:
    print("Unit price:", calculate_unit_price(120, 4))
except ValueError as error:
    print("Invalid calculation:", error)

cart: dict[str, int] = {"mouse": 2, "keyboard": 1}
print("DEBUG cart contents:", cart)
print("Total items:", sum(cart.values()))
