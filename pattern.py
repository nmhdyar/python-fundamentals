a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))

import time

for i in range(a):  # حلقه برای سطرها
    for j in range(b):  # حلقه برای ستون‌ها
        time.sleep(1)
        print("*", end=" ")
    print()  # بعد از تمام شدن هر سطر، خط جدید بگیر
