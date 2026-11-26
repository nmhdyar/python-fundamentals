"""فصل ۰۵.۲ — ماژول‌های کاربردی کتابخانه استاندارد

نکته‌های کلیدی:
- کتابخانه استاندارد همراه پایتون نصب می‌شود و به نصب جداگانه با pip نیاز ندارد.
- math توابع و ثابت‌های ریاضی فراهم می‌کند.
- random مقادیر شبه‌تصادفی تولید می‌کند؛ برای توکن‌های حساس امنیتی از secrets استفاده کن.
- datetime تاریخ و زمان را نمایش می‌دهد و pathlib با مسیرهای فایل کار می‌کند.
"""

from datetime import date
from pathlib import Path
import math
import random

radius: float = 2.5
print(f"Area: {math.pi * radius ** 2:.2f}")
random.seed(7)
print("Sample:", random.randint(1, 6))

project_path: Path = Path("my_project")
print("Folder name:", project_path.name)
print("Today:", date.today())
