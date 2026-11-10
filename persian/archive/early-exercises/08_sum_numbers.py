# این برنامه مجموع اعداد ۱ تا ۱۰۰ را با حلقه for محاسبه و چاپ می‌کند.

total: int = 0

for number in range(1, 101):
    total = total + number

print("مجموع:", total)
