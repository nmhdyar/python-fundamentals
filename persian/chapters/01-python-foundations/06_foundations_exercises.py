"""
فصل ۰۱.۶ — تمرین‌های مبانی

پیش از دیدن هر راه‌حلی، خودت مسئله را حل کن.
Type Hint نوع مورد انتظار را مشخص می‌کند؛ ورودی را اعتبارسنجی یا تبدیل نمی‌کند.
"""

# تمرین ۱: پروفایل شخصی
# نام، سن و شهر کاربر را دریافت کن.
# یک پروفایل مرتب نمایش بده و سن او در سال آینده را محاسبه کن.

print("تمرین ۱ — پروفایل شخصی")

name: str = input("نام: ").strip()
age_text: str = input("سن: ")
age: int = int(age_text)
city: str = input("شهر: ").strip()

print("\n" + "=" * 30)
print(f"پروفایل: {name.title()}")
print("=" * 30)
print(f"شهر: {city.title()}")
print(f"سن فعلی: {age}")
print(f"سن در سال آینده: {age + 1}")

print("\n" + "-" * 40 + "\n")

# تمرین ۲: محاسبه‌گر خرید
# نام کالا، قیمت و تعداد را دریافت کن.
# مبلغ اولیه، تخفیف ۱۰ درصدی و مبلغ نهایی را محاسبه کن.

print("تمرین ۲ — محاسبه‌گر خرید")

item_name: str = input("نام کالا: ").strip()
item_price_text: str = input("قیمت کالا: ")
item_price: float = float(item_price_text)
item_quantity_text: str = input("تعداد: ")
item_quantity: int = int(item_quantity_text)

subtotal: float = item_price * item_quantity
discount_rate: float = 0.10
discount_amount: float = subtotal * discount_rate
final_total: float = subtotal - discount_amount

print("\n" + "=" * 30)
print("خلاصه خرید")
print("=" * 30)
print(f"کالا: {item_name.title()}")
print(f"مبلغ اولیه: {subtotal:.2f}")
print(f"تخفیف (۱۰٪): -{discount_amount:.2f}")
print(f"مبلغ نهایی: {final_total:.2f}")

# چالش:
# اعتبارسنجی ورودی را اضافه کن تا قیمت و تعداد منفی پذیرفته نشوند.
