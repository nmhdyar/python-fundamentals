import time

start = time.time()

a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))

for i in range(a):
    for j in range(b):
        if (i + j) % 2 == 0:  # مثلاً شرط رو روی مجموع سطر و ستون می‌ذاریم
            print("*", end=" ")
        else:
            print(" ", end=" ")  # جای خالی برای جایگاه‌های غیرزوج
    print()  # بعد از هر سطر، خط جدید

end = time.time()

print("Execution time:", end - start, "seconds")
