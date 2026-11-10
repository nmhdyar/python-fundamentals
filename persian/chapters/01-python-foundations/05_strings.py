"""
فصل ۰۱.۵ — رشته‌ها

نکته‌های کلیدی:
- رشته‌ها دنباله‌ای از نویسه‌ها هستند.
- اندیس‌گذاری از صفر شروع می‌شود؛ اندیس منفی از انتهای رشته می‌شمارد.
- برش با ساختار [start:stop:step] انجام می‌شود؛ stop در نتیجه قرار نمی‌گیرد.
- رشته‌ها تغییرناپذیرند؛ متدها رشته جدیدی برمی‌گردانند.
- f-string روش خوانایی برای قالب‌بندی مقدارهاست.
"""

# مثال ۱: اندیس‌گذاری، برش و طول رشته
language: str = "Python"

print("نویسه اول:", language[0])
print("نویسه آخر:", language[-1])
print("سه نویسه اول:", language[0:3])
print("از اندیس ۲ به بعد:", language[2:])
print("معکوس:", language[::-1])
print("طول:", len(language))

print("\n" + "-" * 40 + "\n")

# مثال ۲: پاک‌سازی و قالب‌بندی متن ورودی
raw_name: str = "   nImA mahdiYar   "

clean_name: str = raw_name.strip()
display_name: str = clean_name.title()
username: str = clean_name.lower().replace(" ", "_")

print("متن اولیه:", repr(raw_name))
print("نام مرتب‌شده:", display_name)
print("نام کاربری:", username)
print("با Nima شروع می‌شود:", display_name.startswith("Nima"))
print("دارای فاصله است:", " " in display_name)

# رشته‌ها تغییرناپذیرند؛ این دستور یک رشته جدید می‌سازد.
message: str = "hello"
message = message.upper()
print(f"پیام به‌روزشده: {message}")
