"""فصل ۰۵.۳ — شناخت استثناها

نکته‌های کلیدی:
- خطای نحوی مانع تجزیه و فهم کد می‌شود.
- استثنا هنگام اجرای برنامه رخ می‌دهد.
- استثناهای رایج شامل ValueError، TypeError، ZeroDivisionError، KeyError و IndexError هستند.
- ابتدا نوع استثنا و چند خط پایانی Traceback را بخوان.
"""

raw_age: str = "twenty"
try:
    age: int = int(raw_age)
    print("Age:", age)
except ValueError:
    print("The age must contain digits.")

values: list[int] = [10, 20]
try:
    print(values[4])
except IndexError as error:
    print("Index problem:", error)
