"""
فصل ۰۲.۲ — پیمایش با حلقه for

نکته‌های کلیدی:
- حلقه for اعضای یک داده قابل پیمایش را یکی‌یکی بررسی می‌کند.
- range(stop) از صفر شروع می‌شود و stop را شامل نمی‌شود.
- range(start, stop, step) دنباله تولیدشده را کنترل می‌کند.
- نوع مجموعه را مشخص کن؛ پایتون می‌تواند نوع متغیر حلقه را تشخیص دهد.
"""

# مثال ۱: پیمایش یک لیست
languages: list[str] = ["Python", "JavaScript", "Java", "C++"]

for language in languages:
    print("در حال یادگیری:", language)

print("\n" + "-" * 40 + "\n")

# مثال ۲: تولید دنباله‌ای از اعداد زوج
start: int = 2
stop: int = 11
step: int = 2

for number in range(start, stop, step):
    print(number)

# مقدار stop یعنی ۱۱ در خروجی قرار نمی‌گیرد.
