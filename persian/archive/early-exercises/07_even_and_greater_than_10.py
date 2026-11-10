# چاپ اعداد زوج بزرگ‌تر از ۱۰

for number in range(1, 31):
    if number % 2 == 0 and number > 10:
        print("عدد زوج موردنظر:", number)
