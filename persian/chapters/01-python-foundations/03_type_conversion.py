"""
فصل ۰۱.۳ — تبدیل نوع داده

نکته‌های کلیدی:
- توابع int()، float() و str() مقدارهای سازگار را تبدیل می‌کنند.
- چون input() رشته برمی‌گرداند، ورودی عددی معمولاً به تبدیل نوع نیاز دارد.
- تابع bool() از قواعد ارزش منطقی پیروی می‌کند؛ رشته غیرخالی True است.
- تبدیل نامعتبر ممکن است خطای ValueError ایجاد کند.
- Type Hint نوع را توصیف می‌کند و خودش تبدیل انجام نمی‌دهد.
"""

# مثال ۱: تبدیل ورودی کاربر پیش از انجام محاسبات
age_text: str = input("سن خود را وارد کن: ")
age: int = int(age_text)

next_year_age: int = age + 1

print(f"سال آینده {next_year_age} ساله خواهی شد.")

height_text: str = input("قد خود را بر حسب متر وارد کن (مثلاً 1.82): ")
height: float = float(height_text)

print(f"قد تو {height:.2f} متر است.")

print("\n" + "-" * 40 + "\n")

# مثال ۲: تبدیل مقدارها و شناخت تبدیل بولی
score: float = 87.9
whole_score: int = int(score)  # int بخش اعشاری را حذف می‌کند و گرد نمی‌کند.
score_text: str = str(score)

print("مقدار اصلی:", score, type(score))
print("به شکل عدد صحیح:", whole_score, type(whole_score))
print("به شکل متن:", score_text, type(score_text))

print(bool(0))       # False
print(bool(12))      # True
print(bool(""))      # False
print(bool("False")) # True؛ چون این رشته خالی نیست!

# در برنامه‌های واقعی، پیش از تبدیل نوع ورودی کاربر را اعتبارسنجی کن.
