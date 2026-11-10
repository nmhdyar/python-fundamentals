# رسم الگوی شطرنجی و اندازه‌گیری زمان اجرای برنامه

import time

start: float = time.time()

rows: int = int(input("تعداد سطرها را وارد کن: "))
columns: int = int(input("تعداد ستون‌ها را وارد کن: "))

for row in range(rows):
    for column in range(columns):
        if (row + column) % 2 == 0:  # مجموع اندیس سطر و ستون زوج است.
            print("*", end=" ")
        else:
            print(" ", end=" ")  # برای خانه‌های دیگر یک فاصله چاپ کن.
    print()  # پس از هر سطر به خط بعد برو.

end: float = time.time()

print("زمان اجرای برنامه:", end - start, "ثانیه")
