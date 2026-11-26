"""فصل ۰۳.۲ — تاپل‌ها

نکته‌های کلیدی:
- تاپل مرتب و تغییرناپذیر است.
- تاپل تک‌عضوی به ویرگول پایانی نیاز دارد.
- بازکردن تاپل (Unpacking) اعضا را به چند نام اختصاص می‌دهد.
- برای داده‌های ثابت یا مقادیری که نباید با اندیس تغییر کنند، از تاپل استفاده کن.
"""

# مثال ۱: ذخیره مختصات ثابت
point: tuple[float, float] = (10.5, 4.2)
x_coordinate, y_coordinate = point

print("X:", x_coordinate)
print("Y:", y_coordinate)

# مثال ۲: برگرداندن چند مقدار از تابع
def get_user() -> tuple[str, int]:
    return "Nima", 20

user_name, user_age = get_user()
print(f"{user_name} is {user_age} years old.")

# تاپل تک‌عضوی:
single_value: tuple[str] = ("Python",)
print(single_value)
