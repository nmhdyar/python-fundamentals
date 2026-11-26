"""فصل ۰۵.۴ — مدیریت استثناها

نکته‌های کلیدی:
- فقط عملیات پرخطر را داخل بلوک try قرار بده.
- به‌جای except خالی، نوع استثنای مشخص را بگیر.
- بلوک else زمانی اجرا می‌شود که استثنایی رخ نداده باشد.
- بلوک finally چه استثنا رخ بدهد چه ندهد اجرا می‌شود.
"""

def parse_quantity(text: str) -> int | None:
    try:
        quantity = int(text)
    except ValueError:
        print("Quantity must be a whole number.")
        return None
    else:
        if quantity < 0:
            print("Quantity cannot be negative.")
            return None
        return quantity
    finally:
        print("Input check finished.")

print("Result:", parse_quantity("4"))
print("Result:", parse_quantity("four"))
