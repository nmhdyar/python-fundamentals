"""
فصل ۰۱.۴ — عملگرها

نکته‌های کلیدی:
- حسابی: +، -، *، /، //، %، **
- مقایسه‌ای: ==، !=، >، <، >=، <=
- منطقی: and، or، not
- انتساب: =، +=، -=، *= و ...
- پرانتزها ترتیب محاسبات را روشن‌تر می‌کنند.
"""

# مثال ۱: عملگرهای حسابی
first_number: int = 17
second_number: int = 5

print("جمع:", first_number + second_number)
print("تفریق:", first_number - second_number)
print("ضرب:", first_number * second_number)
print("تقسیم:", first_number / second_number)
print("تقسیم صحیح:", first_number // second_number)
print("باقی‌مانده:", first_number % second_number)
print("توان:", first_number ** 2)

print("\n" + "-" * 40 + "\n")

# مثال ۲: ترکیب عملگرهای مقایسه‌ای و منطقی برای تصمیم‌گیری
age: int = 20
has_ticket: bool = True
is_vip: bool = False

is_adult: bool = age >= 18
can_enter: bool = is_adult and (has_ticket or is_vip)

print("بزرگسال است:", is_adult)
print("بلیت دارد:", has_ticket)
print("مهمان ویژه است:", is_vip)
print("اجازه ورود دارد:", can_enter)

# عملگرهای انتساب مقدار یک متغیر موجود را به‌روزرسانی می‌کنند.
balance: int = 100
balance += 25
balance -= 10
balance *= 2

print("موجودی نهایی:", balance)

# برای خوانایی عبارت‌های پیچیده از پرانتز استفاده کن.
result: int = (10 + 5) * 2
print("نتیجه:", result)
