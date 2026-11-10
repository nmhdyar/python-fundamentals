"""
فصل ۰۲.۷ — حلقه‌های تو در تو

نکته‌های کلیدی:
- حلقه تو در تو یعنی یک حلقه داخل حلقه دیگر قرار بگیرد.
- حلقه بیرونی معمولاً سطرها را کنترل می‌کند.
- حلقه داخلی معمولاً ستون‌ها را کنترل می‌کند.
- حلقه داخلی پیش از رفتن حلقه بیرونی به تکرار بعدی، تمام می‌شود.
- range() اندیس‌های صحیح سطر و ستون را تولید می‌کند.
"""

# مثال ۱: رسم یک مستطیل
rows: int = 3
columns: int = 5

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()

print("\n" + "-" * 40 + "\n")

# مثال ۲: چاپ مختصات سطر و ستون
first_index: int = 1
last_index: int = 4

for row in range(first_index, last_index):
    for column in range(first_index, last_index):
        print(f"({row}, {column})", end=" ")
    print()
