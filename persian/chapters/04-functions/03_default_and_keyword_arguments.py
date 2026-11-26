"""فصل ۰۴.۳ — آرگومان‌های پیش‌فرض و نام‌دار

نکته‌های کلیدی:
- مقدار پیش‌فرض بعضی آرگومان‌ها را اختیاری می‌کند.
- آرگومان نام‌دار خوانایی فراخوانی تابع را بیشتر می‌کند.
- پارامترهای اجباری باید پیش از پارامترهای دارای مقدار پیش‌فرض بیایند.
- از مقدار پیش‌فرض تغییرپذیر مانند [] یا {} استفاده نکن.
"""

def create_profile(name: str, city: str = "Unknown", active: bool = True) -> dict[str, object]:
    return {"name": name, "city": city, "active": active}

profile_one = create_profile("Sara")
print(profile_one)

profile_two = create_profile("Nima", active=False, city="Shiraz")
print(profile_two)
