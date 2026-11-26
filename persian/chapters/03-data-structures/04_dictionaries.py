"""فصل ۰۳.۴ — دیکشنری‌ها

نکته‌های کلیدی:
- دیکشنری کلیدهای هش‌پذیر و یکتا را به مقدارها نگاشت می‌کند.
- وقتی مطمئنی کلید وجود دارد از [] و وقتی ممکن است وجود نداشته باشد از get() استفاده کن.
- متدهای keys، values و items نماهایی از دیکشنری ارائه می‌کنند.
- متدهای update و pop و عملگر in از عملیات رایج هستند.
"""

# مثال ۱: خواندن و به‌روزرسانی محصول
product: dict[str, object] = {
    "name": "Keyboard",
    "price": 49.90,
    "stock": 12,
}

print("Product:", product["name"])
print("Category:", product.get("category", "Uncategorized"))

product["stock"] = 10
product["category"] = "Accessories"
print("Updated product:", product)

# مثال ۲: شمارش تعداد تکرار کلمات
words: list[str] = ["python", "api", "python", "web", "api", "python"]
word_counts: dict[str, int] = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(f"{word}: {count}")
