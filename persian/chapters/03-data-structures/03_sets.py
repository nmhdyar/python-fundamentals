"""فصل ۰۳.۳ — مجموعه‌ها (Sets)

نکته‌های کلیدی:
- مجموعه فقط مقادیر هش‌پذیر و یکتا نگه می‌دارد و اندیس موقعیتی ندارد.
- برای ساخت مجموعه خالی از set() استفاده کن؛ {} یک دیکشنری خالی می‌سازد.
- بررسی عضویت برای جست‌وجوی سریع کاربرد دارد.
- اجتماع، اشتراک و تفاضل مجموعه‌ها را مقایسه می‌کنند.
"""

# مثال ۱: حذف برچسب‌های تکراری
tags: list[str] = ["python", "web", "python", "api", "web"]
unique_tags: set[str] = set(tags)

print("Unique tags:", unique_tags)
print("Has API tag:", "api" in unique_tags)

# مثال ۲: مقایسه ثبت‌نام دوره‌ها
morning_group: set[str] = {"Sara", "Ali", "Nima"}
evening_group: set[str] = {"Nima", "Mina", "Reza"}

print("All students:", morning_group | evening_group)
print("Both groups:", morning_group & evening_group)
print("Morning only:", morning_group - evening_group)
