"""
فصل ۰۱.۱ — متغیرها و انواع داده

نکته‌های کلیدی:
- متغیر نامی است که به یک مقدار اشاره می‌کند.
- پایتون نوع‌دهی پویا دارد؛ یک متغیر می‌تواند در زمان‌های مختلف به مقادیر با نوع‌های متفاوت اشاره کند.
- برای نام متغیرها از نام‌های معنادار و سبک snake_case استفاده کن.
- نوع‌های داخلی رایج: int، float، str، bool و NoneType.
- Type Hint نوع مورد انتظار را مستند می‌کند، اما هنگام اجرا آن را اجباری نمی‌کند.
"""

# مثال ۱: ساخت متغیر و بررسی نوع آن‌ها
student_name: str = "Nima"
student_age: int = 20
student_height: float = 182.5
is_learning_python: bool = True
middle_name: str | None = None

print("نام دانشجو:", student_name)
print("سن:", student_age)
print("قد:", student_height)
print("در حال یادگیری پایتون:", is_learning_python)

print(type(student_name))       # <class 'str'>
print(type(student_age))        # <class 'int'>
print(type(student_height))     # <class 'float'>
print(type(is_learning_python)) # <class 'bool'>
print(type(middle_name))        # <class 'NoneType'>

print("\n" + "-" * 40 + "\n")

# مثال ۲: به‌روزرسانی و مقداردهی دوباره به متغیرها
product_name: str = "Keyboard"
price: float = 45.90
quantity: int = 3
in_stock: bool = True

total_price: float = price * quantity

print(f"کالا: {product_name}")
print(f"تعداد: {quantity}")
print(f"مبلغ کل: {total_price:.2f}")

# مقداردهی دوباره، مقدار مورد اشاره متغیر را تغییر می‌دهد.
quantity = 5
total_price = price * quantity

print(f"تعداد جدید: {quantity}")
print(f"مبلغ کل جدید: {total_price:.2f}")

# قواعد نام‌گذاری:
# - نام باید با حرف یا زیرخط شروع شود.
# - در نام متغیر فاصله یا کلمه رزروشده پایتون قرار نده.
# - نام‌های توصیفی و سبک snake_case را ترجیح بده.
