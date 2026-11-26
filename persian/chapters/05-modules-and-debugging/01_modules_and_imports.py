"""فصل ۰۵.۱ — ماژول‌ها و Import

نکته‌های کلیدی:
- ماژول یک فایل پایتون است که نام‌ها و تعریف‌ها را در خود دارد.
- import module نام‌ها را در فضای نام ماژول نگه می‌دارد.
- from module import name یک نام مشخص را وارد می‌کند.
- از main guard برای جداکردن تعریف‌های قابل استفاده مجدد از اجرای اسکریپت استفاده کن.
"""

import math
from statistics import mean as calculate_mean

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

def main() -> None:
    print(f"Circle area: {circle_area(3):.2f}")
    print("Mean:", calculate_mean([10, 20, 30]))

if __name__ == "__main__":
    main()
