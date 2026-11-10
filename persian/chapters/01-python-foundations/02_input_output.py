"""
فصل ۰۱.۲ — ورودی و خروجی

نکته‌های کلیدی:
- تابع input() همیشه یک رشته برمی‌گرداند.
- تابع print() مقدارها را نمایش می‌دهد.
- f-string قالب‌بندی خروجی را خواناتر می‌کند.
- تابع print() آرگومان‌های sep و end را نیز پشتیبانی می‌کند.
- با Type Hint نوع داده‌ای را که ذخیره می‌کنی مشخص کن.
"""

# مثال ۱: دریافت اطلاعات و نمایش یک پیام قالب‌بندی‌شده
first_name: str = input("نام خود را وارد کن: ")
city: str = input("در کدام شهر زندگی می‌کنی؟ ")

print(f"سلام {first_name}!")
print(f"شهر محل زندگی تو {city} است.")

print("\n" + "-" * 40 + "\n")

# مثال ۲: ساخت یک رسید ساده
product: str = input("نام کالا: ")
unit_price_text: str = input("قیمت هر واحد: ")
quantity_text: str = input("تعداد: ")

# تبدیل نوع به‌صورت کامل در درس بعد بررسی می‌شود.
unit_price: float = float(unit_price_text)
quantity: int = int(quantity_text)

total: float = unit_price * quantity

print("\nرسید خرید")
print("=" * 25)
print("کالا:", product)
print("قیمت هر واحد:", f"{unit_price:.2f}")
print("تعداد:", quantity)
print("مبلغ کل:", f"{total:.2f}")

# sep جداکننده بین مقادیر را مشخص می‌کند.
print("Python", "is", "fun", sep=" | ")

# end مشخص می‌کند print() در انتهای خروجی چه چیزی اضافه کند.
print("در حال بارگذاری", end="...")
print("انجام شد!")
