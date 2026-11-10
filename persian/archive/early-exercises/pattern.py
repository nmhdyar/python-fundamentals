# رسم مستطیل با حلقه‌های تو در تو و مکث بین چاپ ستاره‌ها

import time

rows: int = int(input("تعداد سطرها را وارد کن: "))
columns: int = int(input("تعداد ستون‌ها را وارد کن: "))

for row in range(rows):  # حلقه مربوط به سطرها
    for column in range(columns):  # حلقه مربوط به ستون‌ها
        time.sleep(1)
        print("*", end=" ")
    print()  # پس از پایان هر سطر، به خط بعد برو
