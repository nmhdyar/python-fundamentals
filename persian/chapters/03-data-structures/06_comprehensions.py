"""فصل ۰۳.۶ — Comprehensionها

نکته‌های کلیدی:
- List Comprehension از یک داده قابل پیمایش، لیست می‌سازد.
- برای فیلترکردن اعضا می‌توان شرط if اضافه کرد.
- Dictionary Comprehension جفت‌های کلید و مقدار تولید می‌کند.
- اگر کامپرهنشن خوانایی کمی داشت، حلقه معمولی انتخاب بهتری است.
"""

# مثال ۱: تبدیل و فیلترکردن اعداد
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
squares_of_evens: list[int] = [
    number ** 2 for number in numbers if number % 2 == 0
]
print("Even squares:", squares_of_evens)

# مثال ۲: ساخت دیکشنری از نام‌ها
names: list[str] = ["sara", "ali", "nima"]
name_lengths: dict[str, int] = {
    name: len(name) for name in names
}
print("Name lengths:", name_lengths)
