# practice.py
# 1. Store an expense name (str), amount (float), and paid flag (bool)
# 2. Calculate: if amount > 50, print "big expense", else "small expense"
# 3. Use modulo to check if amount is a whole number (amount % 1 == 0)

expense_name = "Shopping"
amount = 80.0
paid_flag = True

category = "big expense" if amount > 50 else "small expense"
print(category)

number_type = "whole number" if amount % 1 == 0 else "has cents"
print(f"{amount} is a {number_type}")