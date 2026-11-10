"""
فصل ۰۲.۵ — ترکیب شرط‌ها

نکته‌های کلیدی:
- and: همه شرط‌ها باید True باشند.
- or: حداقل یکی از شرط‌ها باید True باشد.
- not: مقدار بولی را معکوس می‌کند.
- پرانتزها خوانایی عبارت‌های پیچیده را بیشتر می‌کنند.
- عبارت‌های شرطی نتیجه‌ای از نوع bool تولید می‌کنند.
"""

# مثال ۱: پیدا کردن اعداد زوج بزرگ‌تر از ۱۰
for number in range(1, 31):
    is_even: bool = number % 2 == 0
    is_greater_than_ten: bool = number > 10

    if is_even and is_greater_than_ten:
        print("عدد موردنظر:", number)

print("\n" + "-" * 40 + "\n")

# مثال ۲: تصمیم‌گیری درباره اجازه ورود یک مراجعه‌کننده
age: int = 20
has_ticket: bool = False
is_vip: bool = True

if age >= 18 and (has_ticket or is_vip):
    print("اجازه ورود صادر شد.")
else:
    print("اجازه ورود صادر نشد.")
