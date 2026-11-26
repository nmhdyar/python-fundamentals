"""فصل ۰۳.۱ — لیست‌ها

نکته‌های کلیدی:
- لیست مرتب و تغییرپذیر است.
- اندیس از صفر شروع می‌شود؛ اندیس منفی از انتهای لیست می‌شمارد.
- برش (Slice) یک لیست جدید می‌سازد.
- متدهای append، extend، insert، remove، pop، sort و copy کاربرد زیادی دارند.
"""

# مثال ۱: خواندن و تغییر فهرست خرید
shopping_list: list[str] = ["bread", "milk", "eggs"]
print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])

shopping_list.append("coffee")
shopping_list[1] = "oat milk"
print("Updated list:", shopping_list)

# مثال ۲: برش و مرتب‌سازی بدون تغییر لیست اصلی
scores: list[int] = [72, 95, 81, 68, 88]
top_scores: list[int] = sorted(scores, reverse=True)[:3]

print("Original scores:", scores)
print("Top three:", top_scores)
