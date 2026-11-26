"""فصل ۰۴.۶ — بازگشت، Docstring و Type Hint

نکته‌های کلیدی:
- تابع بازگشتی خودش را با مسئله‌ای کوچک‌تر یا ساده‌تر فراخوانی می‌کند.
- هر طراحی بازگشتی معتبر به حالت پایه نیاز دارد.
- Docstring هدف و رفتار تابع را توضیح می‌دهد.
- Type Hint انتظار ما را مستند می‌کند؛ پایتون آن را به‌صورت خودکار اجبار نمی‌کند.
"""

def factorial(number: int) -> int:
    """فاکتوریل یک عدد صحیح نامنفی را برمی‌گرداند."""
    if number < 0:
        raise ValueError("number must not be negative")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)

def countdown(number: int) -> None:
    """اعداد را تا صفر چاپ می‌کند."""
    if number < 0:
        return
    print(number)
    if number > 0:
        countdown(number - 1)

print("5! =", factorial(5))
countdown(3)
