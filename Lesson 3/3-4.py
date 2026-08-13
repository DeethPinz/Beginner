is_member = True
purchase_total = 120

if is_member and purchase_total >= 100:
    print("Discount applies")
else:
    print("No discount")

has_coupon = True
is_vip = True

if has_coupon or is_vip:
    print("Discount applies")
else:
    print("No discount")

if has_coupon and is_vip:
    print("Both discounts apply")
else:
    None

is_locked = False
if not is_locked:
    print("You can open the door")
else:
    print("Can't open the door")